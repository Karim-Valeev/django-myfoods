import logging

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import IntegrityError
from django.shortcuts import render, redirect
from django.views.generic import DetailView

from main.forms import BasketForm
from main.models.basket import Basket, Status

logger = logging.getLogger(__name__)


@login_required()
def basket_list_page(request):
    baskets = Basket.objects.filter(owner=request.user)
    return render(request, "main/basket/baskets.html", {"baskets": baskets})


@login_required()
def create_basket(request):
    message = ""
    if request.method == "POST":
        form = BasketForm(request.POST)
        basket = Basket()
        if form.is_valid():
            basket.name = form.cleaned_data["name"]
            basket.delivery_address = form.cleaned_data["delivery_address"]
            basket.status = Status.objects.get(name="Filling")
            basket.owner = request.user

            favourite = request.POST.get("favourite")
            basket.favourite = favourite == "on"
            try:
                basket.save()
            except IntegrityError:
                logger.error("IntegrityError: duplicate key value violates unique constraint during basket creation")
                message = "try to create basket one more time, please"
        else:
            form = BasketForm()
            message = "form not valid"
        baskets = Basket.objects.filter(owner=request.user)
        return render(
            request,
            "main/basket/baskets.html",
            {
                "baskets": baskets,
                "form": form,
                "message": message,
            },
        )
    return redirect("baskets")


class BasketPageDetailView(LoginRequiredMixin, DetailView):
    model = Basket
    context_object_name = "basket"
    template_name = "main/basket/basket-page.html"
    pk_url_kwarg = "basket_id"
