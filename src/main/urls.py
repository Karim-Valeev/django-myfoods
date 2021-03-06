from django.urls import path, re_path

from main.views import *

urlpatterns = [
    path("", main_page, name="main"),
    path("about/", about_page, name="about"),
    path("login/", login_view, name="login"),
    path("register/", reg_view, name="register"),
    path("profile/", profile_view, name="profile"),
    path("profile/add_favourite_category/", add_favourite_category, name="add_favourite_category"),
    path("profile/baskets/", basket_list_page, name="baskets"),
    path("profile/baskets/create", create_basket, name="create_basket"),
    re_path(r"^profile/baskets/(?P<basket_id>[0-9]+)$", BasketPageDetailView.as_view(), name="basket"),
    path("shops/", ShopListView.as_view(), name="shops"),
    path("shop/items/", ShopItemListView.as_view(), name="shop_items"),
    path("shop/items/<item_id>/", item_page, name="item"),
    path("shop/items/add_comment/", add_comment, name="add_comment"),
    path("shop/items/like/<int:item_id>", like, name="like"),
    path("shop/items/dislike/<int:item_id>", dislike, name="dislike"),
    path("sales/", SaleListView.as_view(), name="sales"),
    path("logout/", logout_view, name="logout"),
]
