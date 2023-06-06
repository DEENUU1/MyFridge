from fak.models import Fak, Medicine
import datetime
import pytest
from django.contrib.auth import get_user_model


@pytest.fixture
def user():
    User = get_user_model()
    return User.objects.create(username="testuser")


@pytest.fixture
def fak(user):
    return Fak.objects.create(name="Test Fak", author=user)


@pytest.mark.django_db
def test_model_fak_successfully_created(user):
    fak = Fak.objects.create(name="Fak 1", author=user)
    assert fak.name == "Fak 1"
    assert fak.__str__() == "Fak 1"


@pytest.fixture
def medicine(fak, user):
    return Medicine.objects.create(
        name="Test Medicine",
        expiration_date=datetime.date.today() + datetime.timedelta(days=7),
        quantity="MEDIUM",
        fak=fak,
        author=user,
    )


@pytest.mark.django_db
def test_medicine_expiration_date_info_expired(medicine):
    medicine.expiration_date = datetime.date.today() - datetime.timedelta(days=1)
    medicine.save()
    assert medicine.get_expiration_date_info == "Expired"


@pytest.mark.django_db
def test_medicine_expiration_date_info_upcoming(medicine):
    medicine.expiration_date = datetime.date.today() + datetime.timedelta(days=6)
    medicine.save()
    assert (
        medicine.get_expiration_date_info == "Attention, expiration date is coming soon"
    )


@pytest.mark.django_db
def test_medicine_expiration_date_info_valid(medicine):
    medicine.expiration_date = datetime.date.today() + datetime.timedelta(days=10)
    medicine.save()
    assert medicine.get_expiration_date_info == str(medicine.expiration_date)
