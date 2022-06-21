from django.urls import path, re_path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework.routers import SimpleRouter, DefaultRouter
from rest_framework_simplejwt import views as jwt_views

from api.views import *


# роутер нужен, чтобы сгенерить урлы под вью сет и самому их не прописывать соотвественно
router = SimpleRouter()
router.register("baskets", BasketViewSet, "baskets")

schema_view = get_schema_view(
    openapi.Info(
        title="MyFoods API",
        default_version="v0",
        description="Testing Django Rest Framework",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
)

urlpatterns = [
    path("check/", check_api_view, name="check-api"),
    path("token/", jwt_views.TokenObtainPairView.as_view(), name="token-obtain-pair"),
    path("token/refresh/", jwt_views.TokenRefreshView.as_view(), name="token-refresh"),
    *router.urls,
    re_path(r"swagger(?P<format>\.json|\.yaml)$", schema_view.without_ui(cache_timeout=0), name="schema-json"),
    path("swagger/", schema_view.with_ui("swagger", cache_timeout=0), name="schema-swagger-ui"),
    path("redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
]
