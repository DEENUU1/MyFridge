import pytest
from django.urls import reverse
from django.test import RequestFactory
from users.models import CustomUser
from dishes.models import Dish
from dishes.views import HomeView, DishCreateView, UpdateDishView, DeleteDishView, DishDetailView
from .test_models import dish_data

pytestmark = pytest.mark.django_db


@pytest.fixture
def user():
    return CustomUser.objects.create_user(username="testuser", password="testpass")


@pytest.fixture
def factory():
    return RequestFactory()


def test_home_view(client, factory):
    url = reverse("dishes:home")
    request = factory.get(url)
    response = HomeView.as_view()(request)
    assert response.status_code == 200


def test_dish_detail_view(client, factory, dish_data):
    url = reverse("dishes:dish-detail", kwargs={"pk": dish_data.pk})
    request = factory.get(url)
    response = DishDetailView.as_view()(request, pk=dish_data.pk)
    assert response.status_code == 200


def test_dish_create_view(client, factory, user):
    url = reverse("dishes:dish-create")
    request = factory.post(url, data={"name": "New Dish"})
    request.user = user
    response = DishCreateView.as_view()(request)
    assert response.status_code == 200

