from django.core.mail import send_mail

from main.models import User, Sale
from myfoods import settings
from myfoods.celery import app


@app.task(queue="default")
def send_sales():
    users = User.objects.all().prefetch_related("favourite_categories")
    for user in users:
        category_pk_list = user.favourite_categories.values_list("id", flat=True)
        sales = Sale.objects.filter(item__category_id__in=category_pk_list)
        message = ""
        if len(sales) > 0:
            for sale in sales:
                str_value = f"{int(sale.value * 100)}%"
                message += (
                    f"{str_value} sale on {sale.item.name} in {sale.item.shop.name}, {sale.item.shop.address}!\r\n"
                )
            print(message)
            send_mail(
                "Weekly sales from your favorite service MyFoods!",
                message,
                settings.DEFAULT_FROM_EMAIL,
                [user.email],
                fail_silently=True,
            )
    return True
