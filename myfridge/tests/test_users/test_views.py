from contact.views import ContactSuccessView, ContactStatueView
from django.urls import reverse
from django.test import RequestFactory
from test_data.models_fixtures import factory, user, client, user_inactive
import pytest


def test_users_success_register_view_get_method_returns_200_status_code(factory):
    request = factory.get(reverse("users:success_register"))
    view = ContactSuccessView.as_view(template_name="success_register.html")
    response = view(request)
    assert response.status_code == 200


def test_users_statute_view_get_method_returns_200_status_code(factory):
    request = factory.get(reverse("users:statute"))
    view = ContactSuccessView.as_view(template_name="statute.html")
    response = view(request)
    assert response.status_code == 200


def test_users_success_password_change_view_get_method_returns_200_status_code(factory):
    request = factory.get(reverse("users:success_password_change"))
    view = ContactSuccessView.as_view(template_name="password_change_success.html")
    response = view(request)
    assert response.status_code == 200


@pytest.mark.django_db
def test_register_view(client):
    response = client.get(reverse("users:register"))
    assert response.status_code == 200


@pytest.mark.django_db
def test_success_register_view(client):
    response = client.get(reverse("users:success_register"))
    assert response.status_code == 200


@pytest.mark.django_db
def test_login_view(client, user):
    response = client.post(
        reverse("users:login"), {"username": "testuser", "password": "12345"}
    )
    assert response.status_code == 200


@pytest.mark.django_db
def test_logout_view(client, user):
    client.login(username="testuser", password="12345")
    response = client.get(reverse("users:logout"))
    assert response.status_code == 302  # It should redirect after logout


@pytest.mark.django_db
def test_statute_view(client):
    response = client.get(reverse("users:statute"))
    assert response.status_code == 200


@pytest.mark.django_db
def test_change_password_view(client, user):
    client.login(username="testuser", password="12345")
    response = client.get(reverse("users:change_password"))
    assert response.status_code == 200


@pytest.mark.django_db
def test_success_password_change_view(client):
    response = client.get(reverse("users:success_password_change"))
    assert response.status_code == 200


@pytest.mark.django_db
def test_delete_account_view(client, user):
    client.login(username="testuser", password="12345")
    response = client.get(reverse("users:delete_account"))
    assert response.status_code == 200


@pytest.mark.django_db
def test_success_delete_account_view(client):
    response = client.get(reverse("users:success_delete_account"))
    assert response.status_code == 200


@pytest.mark.django_db
def test_user_profile_view(client, user):
    client.login(username="testuser", password="12345")
    response = client.get(reverse("users:profile"))
    assert response.status_code == 302


@pytest.mark.django_db
def test_update_profile_view(client, user):
    client.login(username="testuser", password="12345")
    response = client.get(reverse("users:edit_profile", kwargs={"pk": user.pk}))
    assert response.status_code == 302
