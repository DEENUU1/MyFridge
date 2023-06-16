from contact.views import ContactSuccessView, ContactStatueView
from django.urls import reverse
from django.test import RequestFactory
import pytest
from django.urls import reverse
from django.test import RequestFactory
from contact.views import ContactFormView
from contact.models import Contact, ContactSubject
from contact.forms import ContactForm


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


@pytest.fixture
def contact_subject():
    subject = ContactSubject.objects.create(name="General Inquiry")
    return subject


@pytest.fixture
def valid_form_data(contact_subject):
    data = {
        "username": "John Doe",
        "email": "johndoe@example.com",
        "subject": contact_subject.id,
        "message": "This is a test message.",
        "accept_statute": True,
    }
    return data


@pytest.fixture
def invalid_form_data():
    data = {
        "username": "",
        "email": "invalidemail",
        "subject": "",
        "message": "",
        "accept_statute": False,
    }
    return data


@pytest.fixture
def factory():
    return RequestFactory()


@pytest.mark.django_db
def test_contact_form_view_valid_form(factory, contact_subject, valid_form_data):
    url = reverse("contact:contact")
    request = factory.post(url, data=valid_form_data)
    response = ContactFormView.as_view()(request)
    assert response.status_code == 302
    assert response.url == reverse("contact:contact-success")

    assert Contact.objects.count() == 1
    contact = Contact.objects.first()
    assert contact.username == valid_form_data["username"]
    assert contact.email == valid_form_data["email"]
    assert contact.subject == contact_subject
    assert contact.message == valid_form_data["message"]


@pytest.mark.django_db
def test_contact_form_view_invalid_form(factory, invalid_form_data):
    url = reverse("contact:contact")
    request = factory.post(url, data=invalid_form_data)
    response = ContactFormView.as_view()(request)
    assert response.status_code == 200
    assert response.template_name == ["contact.html"]
    assert Contact.objects.count() == 0


@pytest.mark.django_db
def test_contact_form_view_get_request(factory):
    url = reverse("contact:contact")
    request = factory.get(url)
    response = ContactFormView.as_view()(request)
    assert response.status_code == 200
    assert response.template_name == ["contact.html"]
    assert isinstance(response.context_data["form"], ContactForm)
