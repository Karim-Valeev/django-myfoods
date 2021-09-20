from django import forms
from django.contrib.auth.forms import UserCreationForm
from main.models.user import User
from main.models.basket import Basket
from main.models.item import ItemComment


class AuthForm(forms.Form):
    email = forms.CharField(label='Email')
    password = forms.CharField(label='Password')


class RegForm(UserCreationForm):
    birthdate = forms.DateField(label='День рождения', required=False)
    profile_pic = forms.ImageField(label="Аватарка", required=False)

    class Meta:
        model = User
        fields = ('username', 'email', 'birthdate', 'password1', 'password2',)


class BasketForm(forms.ModelForm):
    favourite = forms.BooleanField(required=False)

    class Meta:
        model = Basket
        fields = ('name', 'delivery_address',)


class CommentForm(forms.ModelForm):
    shop_id = forms.IntegerField()

    class Meta:
        model = ItemComment
        fields = ('item', 'text',)
