import logging

from django.db import IntegrityError
from django.shortcuts import render, redirect
from django.views.generic import ListView

from main.forms import CommentForm
from main.models.item import Item
from main.models.item_tags import Shop
from main.models.sale import Sale

logger = logging.getLogger(__name__)


class ShopListView(ListView):
    model = Shop
    context_object_name = "shops"
    template_name = "main/item/shops.html"


class ShopItemListView(ListView):
    context_object_name = "items"
    template_name = "main/item/shop-items.html"

    def get_queryset(self):
        shop_id = self.request.GET.get("shop_id", 1)
        items = Item.objects.filter(shop_id=shop_id).prefetch_related("comments")
        return items


def item_page(request, item_id):
    try:
        item = Item.objects.get(id=item_id)
    except Item.DoesNotExist:
        return redirect("shops")
    try:
        item_sale = Sale.objects.filter(item_id=item.pk).latest("from_date")
        sale_value = f"{item_sale.value * 100}%"
        price_with_sale = round(item.price * (1 - item_sale.value), 2)
    except Sale.DoesNotExist:
        sale_value, price_with_sale = None, None

    return render(
        request,
        "main/item/item-page.html",
        {"item": item, "price_with_sale": price_with_sale, "sale_value": sale_value},
    )


def add_comment(request):
    shop_id = request.POST.get("shop_id", "1")
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.owner = request.user
            try:
                comment.save()
            except IntegrityError:
                logger.error("IntegrityError: duplicate key value violates unique constraint during comment creation")
    return redirect(f"/shop/items/?shop_id={shop_id}")
