from django.views.generic import ListView

from main.models import Sale


class SaleListView(ListView):
    model = Sale
    context_object_name = 'sales'
    template_name = 'main/item/sales.html'