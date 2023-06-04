import pytest
from contact.models import Contact, ContactSubject


@pytest.mark.django_db
def test_model_contact_subject_successfully_created():
    subject = ContactSubject.objects.create(name="Subject")
    assert subject.name == "Subject"


@pytest.mark.django_db
def test_model_contact_successfully_created():
    subject = ContactSubject.objects.create(name="Subject")
    contact = Contact.objects.create(
        username="Test user",
        email="test_user@example.com",
        subject=subject,
        message="Test message 123",
    )
    assert contact.username == "Test user"
    assert contact.email == "test_user@example.com"
    assert contact.subject == subject
