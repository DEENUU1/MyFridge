from contact.views import ContactSuccessView, ContactStatueView
from django.urls import reverse
from django.test import RequestFactory


def test_contact_success_view_get_method_returns_200_status_code():
    factory = RequestFactory()
    request = factory.get(reverse("contact:contact-success"))
    view = ContactSuccessView.as_view(template_name="contact_success.html")
    response = view(request)
    assert response.status_code == 200


def test_contact_statue_view_get_method_returns_200_status_code():
    factory = RequestFactory()
    request = factory.get(reverse("contact:contact-statute"))
    view = ContactStatueView.as_view(template_name="contact_statue.html")
    response = view(request)
    assert response.status_code == 200
