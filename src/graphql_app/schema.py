import graphene
from graphene_django import DjangoObjectType

from main.models import Basket


class BasketType(DjangoObjectType):
    class Meta:
        model = Basket
        fields = ("id", "name", "delivery_address", "status", "favourite", "created_at")


class BasketQuery(graphene.ObjectType):
    basket = graphene.Field(BasketType, id=graphene.Int())
    all_baskets = graphene.List(BasketType)

    def resolve_all_baskets(root, info):
        return Basket.objects.all()

    def resolve_basket(root, info, id):
        try:
            basket = Basket.objects.get(pk=id)
        except Basket.DoesNotExist:
            basket = None
        return basket


schema = graphene.Schema(query=BasketQuery)
