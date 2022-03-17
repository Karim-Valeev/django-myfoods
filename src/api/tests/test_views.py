import pytest
from django.urls import reverse
from rest_framework.test import APIClient


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
def api_client():
    return APIClient()


@pytest.mark.django_db
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
