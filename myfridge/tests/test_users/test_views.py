from contact.views import ContactSuccessView, ContactStatueView
from django.urls import reverse
from django.test import RequestFactory


def test_users_success_register_view_get_method_returns_200_status_code():
    factory = RequestFactory()
    request = factory.get(reverse("users:success_register"))
    view = ContactSuccessView.as_view(template_name="success_register.html")
    response = view(request)
    assert response.status_code == 200


def test_users_statute_view_get_method_returns_200_status_code():
    factory = RequestFactory()
    request = factory.get(reverse("users:statute"))
    view = ContactSuccessView.as_view(template_name="statute.html")
    response = view(request)
    assert response.status_code == 200


def test_users_success_password_change_view_get_method_returns_200_status_code():
    factory = RequestFactory()
    request = factory.get(reverse("users:success_password_change"))
    view = ContactSuccessView.as_view(template_name="password_change_success.html")
    response = view(request)
    assert response.status_code == 200
