import pytest
from django.urls import reverse
from rest_framework.test import APIClient

from main.models import Basket, Status


@pytest.fixture
def get_password():
    return "Test_pass.2021"


@pytest.fixture
def create_user(db, django_user_model, get_password):
    def make_user(**kwargs):
        kwargs["password"] = get_password
        if "email" not in kwargs:
            kwargs["email"] = "test@test.com"
        return django_user_model.objects.create_user(**kwargs)

    return make_user


@pytest.fixture
def create_filling_status(db):
    status = Status(code=111, name="Filling")
    status.save()
    return status


@pytest.fixture
def create_user_basket(db, create_user, create_filling_status):
    basket = Basket(
        name='Test basket',
        owner=create_user(),
        status=create_filling_status
    )
    basket.save()
    return basket


@pytest.fixture
def api_client():
    return APIClient()


def test_unauthorized_check_api_request(api_client):
    url = reverse("check-api")
    response = api_client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_get_access_token(api_client, create_user, get_password):
    user = create_user()
    url = reverse("token-obtain-pair")
    response = api_client.post(url, {"email": user.email, "password": get_password})
    assert "access" in response.data


def test_swagger_documentation(api_client):
    url = reverse("schema-swagger-ui")
    response = api_client.get(url)
    assert response.status_code == 200


def test_redoc_documentation(api_client):
    url = reverse("schema-redoc")
    response = api_client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_basket_api_view(api_client, create_user_basket):
    url = "http://127.0.0.1:8000/api/v0/baskets/"
    response = api_client.get(url)
    assert "Test basket" == response.data["results"][0]['name']
