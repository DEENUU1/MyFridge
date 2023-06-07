import pytest
from django.urls import reverse
from django.test import RequestFactory
from users.models import CustomUser as User
from fak.views import (
    FakListView,
    FakCreateView,
    FakUpdateView,
    FakDeleteView,
    MedicineCreateView,
    MedicineUpdateView,
    MedicineDeleteView,
    FakDetailsView,
)
from fak.models import Fak, Medicine

@pytest.fixture
def factory():
    return RequestFactory()

@pytest.fixture
def user():
    return User.objects.create(username="testuser")

@pytest.fixture
def fak(user):
    return Fak.objects.create(name="Test Fak", author=user)

@pytest.fixture
def medicine(user, fak):
    return Medicine.objects.create(
        name="Test Medicine",
        expiration_date="2023-06-30",
        quantity="LOW",
        fak=fak,
        author=user,
    )

@pytest.mark.django_db
def test_fak_list_view(factory, user, fak):
    url = reverse("fak:fak_home")
    request = factory.get(url)
    request.user = user
    response = FakListView.as_view()(request)
    assert response.status_code == 200
    assert len(response.context_data["object_list"]) == 1
    assert response.context_data["object_list"][0] == fak

@pytest.mark.django_db
def test_fak_create_view(factory, user):
    url = reverse("fak:fak_create")
    request = factory.get(url)
    request.user = user
    response = FakCreateView.as_view()(request)
    assert response.status_code == 200
    assert response.template_name == ["fak_create.html"]

@pytest.mark.django_db
def test_fak_update_view(factory, user, fak):
    url = reverse("fak:fak_update", kwargs={"pk": fak.pk})
    request = factory.get(url)
    request.user = user
    response = FakUpdateView.as_view()(request, pk=fak.pk)
    assert response.status_code == 200
    assert response.template_name == ["fak_update.html"]

@pytest.mark.django_db
def test_fak_delete_view(factory, user, fak):
    url = reverse("fak:fak_delete", kwargs={"pk": fak.pk})
    request = factory.get(url)
    request.user = user
    response = FakDeleteView.as_view()(request, pk=fak.pk)
    assert response.status_code == 200

@pytest.mark.django_db
def test_medicine_create_view(factory, user, fak):
    url = reverse("fak:medicine_create")
    request = factory.get(url)
    request.user = user
    response = MedicineCreateView.as_view()(request)
    assert response.status_code == 200

@pytest.mark.django_db
def test_medicine_update_view(factory, user, medicine):
    url = reverse("fak:medicine_update", kwargs={"pk": medicine.pk})
    request = factory.get(url)
    request.user = user
    response = MedicineUpdateView.as_view()(request, pk=medicine.pk)
    assert response.status_code == 200
    assert response.template_name == ["medicine_update.html"]

@pytest.mark.django_db
def test_medicine_delete_view(factory, user, medicine):
    url = reverse("fak:medicine_delete", kwargs={"pk": medicine.pk})
    request = factory.get(url)
    request.user = user
    response = MedicineDeleteView.as_view()(request, pk=medicine.pk)
    assert response.status_code == 200

@pytest.mark.django_db
def test_fak_details_view(factory, user, fak):
    url = reverse("fak:fak_detail", kwargs={"pk": fak.pk})
    request = factory.get(url)
    request.user = user
    response = FakDetailsView.as_view()(request, pk=fak.pk)
    assert response.status_code == 200
    assert response.template_name == ["fak_details.html"]
    assert response.context_data["object"] == fak
