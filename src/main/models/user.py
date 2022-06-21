from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin, UserManager as DjangoUserManager
from django.db import models
from djchoices import DjangoChoices, ChoiceItem

# from .item import Item, ItemLike
from main.models.base import BaseModel
from main.models.item_tags import Category


class UserManager(DjangoUserManager):
    def create_user(self, email, password=None, **kwargs):
        user = self.model(email=email)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password=None, **kwargs):
        user = self.model(email=email, is_superuser=True)
        user.set_password(password)
        user.save()
        return user


class Role(DjangoChoices):
    admin = ChoiceItem()
    user = ChoiceItem()


class User(BaseModel, AbstractBaseUser, PermissionsMixin):
    # Чтобы модель работала нормально нужно для нее переопределить UserManager
    objects = UserManager()

    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    role = models.CharField(choices=Role.choices, default=Role.user, max_length=50)
    birthdate = models.DateField(null=True, blank=True)
    profile_pic = models.ImageField(upload_to='', default='default_profile_pic.jpg', blank=True)

    favourite_categories = models.ManyToManyField(
        Category,
        db_table='user_favourite_category',
        verbose_name='Favourite category',
        related_name='favourite_categories'
    )

    likes = models.ManyToManyField(
        'Item',
        through='ItemLike',
        related_name='likes'
    )

    @property
    def is_staff(self):
        return self.is_superuser

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        db_table = 'profile'
        verbose_name = 'User'
        verbose_name_plural = 'Users'
