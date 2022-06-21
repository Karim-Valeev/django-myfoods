from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.permissions import BasePermission, IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from api.serializers import BasketSerializer, BasketCreateSerializer, BasketUpdateSerializer
from main.models import Basket, Status


@api_view(["GET"])
def check_api_view(request):
    """Method for checking api"""
    content = {"status": "ok"}
    return Response(content, status=status.HTTP_200_OK)


class BasketChangeOnlyForOwnerPermission(BasePermission):
    # TODO: Добавь логику апи ключа
    def has_object_permission(self, request, view, obj):
        if not request.user.is_authenticated:
            return False
        return obj.owner_id == request.user.id


# ModelViewSet include a lot of useful mixins such as List, Generic, CRUD
class BasketViewSet(ModelViewSet):
    """All actions with baskets."""

    permission_classes = [BasketChangeOnlyForOwnerPermission]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        owner = self.request.user
        status = Status.objects.get(name="Filling")
        serializer.save(owner=owner, status=status)

    def get_serializer_class(self):
        if self.action == "retrieve":
            return BasketSerializer
        if self.action == "create":
            return BasketCreateSerializer
        if self.action == "update":
            return BasketUpdateSerializer
        return BasketSerializer

    def get_queryset(self):
        user = self.request.user
        qs = Basket.objects.select_related("owner", "status")
        if user.is_authenticated:
            qs = qs.filter(owner=user)
        return qs
