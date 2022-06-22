from django.contrib import admin

from main.models.user import User
from main.models.basket import Basket, Status, Order
from main.models.item import Item, ItemLike, ItemComment, PurchaseHistory
from main.models.item_tags import Shop, Category
from main.models.sale import Sale


class BasketAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "status", "get_owner_name")
    list_display_links = ("id", "name")
    ordering = ("-created_at",)
    search_fields = ("status",)
    list_filter = ("status", "created_at")
    readonly_fields = ("created_at",)

    def get_owner_name(self, instance: Basket):
        return instance.owner.username


class ItemAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "get_shop_name", "get_category_name", "price")
    list_display_links = ("id", "name")
    search_fields = ("name",)
    list_filter = (
        "id",
        "price",
    )

    def get_shop_name(self, instance: Item):
        return instance.shop.__str__()

    get_shop_name.short_description = "SHOP"

    def get_category_name(self, instance: Item):
        return instance.category.name

    get_category_name.short_description = "CATEGORY"


class SaleAdmin(admin.ModelAdmin):
    list_display = ("item", "value", "from_date", "to_date")
    list_filter = ("value",)


admin.site.register(User)
admin.site.register(Shop)
admin.site.register(Item, ItemAdmin)
admin.site.register(ItemComment)
# admin.site.register(ItemCommentLike)
admin.site.register(ItemLike)
admin.site.register(Status)
admin.site.register(Category)
admin.site.register(Basket)
admin.site.register(Order)
admin.site.register(PurchaseHistory)

admin.site.register(Sale, SaleAdmin)
