from functools import reduce
from operator import and_

from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.db.models import Q, F
from django.shortcuts import render, redirect

from main.forms import AuthForm, RegForm
from main.models import Item
from main.models.item_tags import Category


def login_view(request):
    form = None
    if request.method == "POST":
        form = AuthForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]

            user = authenticate(request, email=email, password=password)

            if user is None:
                form.add_error("email", "Неправильный логин или пароль")
            else:
                login(request, user)
                return redirect("profile")
    return render(request, "main/user/login.html", {"form": form})


def reg_view(request):
    form = None
    message = ""
    if request.method == "POST":
        form = RegForm(request.POST, request.FILES)
        if form.is_valid():
            password1 = form.cleaned_data["password1"]
            password2 = form.cleaned_data["password2"]
            if password1 == password2:
                user = form.save(commit=False)
                picture = form.cleaned_data["profile_pic"]
                if picture:
                    user.profile_pic = picture
                try:
                    user.save()
                    login(request, user)
                    return redirect("profile")
                except IntegrityError:
                    message = "Try to register one more time, please"
            else:
                message = "The entered passwords do not match. Try again"
        else:
            message = "Form not valid, something missing"
    return render(
        request,
        "main/user/register.html",
        {
            "form": form,
            "message": message,
        },
    )


@login_required()
def profile_view(request):
    selected_category = None
    remaining_categories = None

    user_favourite_categories = request.user.favourite_categories.all()

    # functional programming: AND: (NOT: AND Q(), NOT: ADD Q())
    query = reduce(and_, (~Q(name=category.name) for category in user_favourite_categories), Q())

    categories = Category.objects.all().filter(query)
    if categories:
        selected_category = categories[0]
        if len(categories) > 1:
            remaining_categories = categories[1:]

    return render(
        request,
        "main/user/profile.html",
        {"selected_category": selected_category, "remaining_categories": remaining_categories},
    )


def logout_view(request):
    logout(request)
    return redirect("login")


@login_required()
def add_favourite_category(request):
    user = request.user
    user_favourite_category_names = user.favourite_categories.values_list("name", flat=True).order_by("id")
    print(user_favourite_category_names)
    if request.method == "POST" and len(user_favourite_category_names) < 5:
        category_name = request.POST.get("category_name")
        if category_name in Category.objects.values_list("name", flat=True).order_by("id"):
            if category_name not in user_favourite_category_names:
                category = Category.objects.get(name=category_name)
                user.favourite_categories.add(category)

    return redirect("profile")


@login_required()
def like(request, item_id):
    try:
        item = Item.objects.select_related("shop").get(id=item_id)
        if item not in request.user.likes.all():
            request.user.likes.add(item)
            # Все равно придется еще один запрос делать в базу
            Item.objects.filter(id=item_id).update(like_counter=F("like_counter") + 1)
            return redirect(f"/shop/items/?shop_id={item.shop.id}")
        else:
            return redirect("shop_items")
    except Item.DoesNotExist:
        return redirect("shop_items")


@login_required()
def dislike(request, item_id):
    try:
        item = Item.objects.select_related("shop").get(id=item_id)
        if item in request.user.likes.all():
            request.user.likes.remove(item)
            # Все равно придется еще один запрос делать в базу
            Item.objects.filter(id=item_id).update(like_counter=F("like_counter") - 1)
            return redirect(f"/shop/items/?shop_id={item.shop.id}")
        else:
            return redirect("shop_items")
    except Item.DoesNotExist:
        return redirect("shop_items")
