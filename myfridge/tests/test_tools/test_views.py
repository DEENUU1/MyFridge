import pytest
from django.urls import reverse
from tools.views import (
    bmiView,
    ShoppingListCreateView,
    ShoppingListUpdateView,
    ShoppingListDeleteView,
    ShoppingListView,
)
from test_data.models_fixtures import (
    authenticated_user,
    client_with_authenticated_user,
    bmi_form_data,
    shopping_list,
    meal_daily_plan,
    meal,
    user,
)


def test_bmiView(client, bmi_form_data):
    response = client.post(reverse("tools:bmi"), bmi_form_data)
    assert response.status_code == 200
    assert "bmi" in response.context
    assert "bmi_result" in response.context


def test_shopping_list_create_viewe_success_response_get_method(
    client_with_authenticated_user,
):
    response = client_with_authenticated_user.get(reverse("tools:shopping_list_create"))
    assert response.status_code == 200


def test_shopping_list_update_view_success_response_get_method(
    client_with_authenticated_user, shopping_list
):
    response = client_with_authenticated_user.get(
        reverse("tools:shopping_list_update", kwargs={"pk": shopping_list.pk})
    )
    assert response.status_code == 200


def test_shopping_list_view_success_response_get_method(
    client_with_authenticated_user, shopping_list
):
    response = client_with_authenticated_user.get(reverse("tools:shopping_list"))
    assert response.status_code == 200
    assert "object_list" in response.context


@pytest.mark.django_db
def test_meal_create_view(client, user):
    client.login(username="testuser", password="testpassword")
    response = client.get(
        reverse("tools:meal_create")
    )
    assert response.status_code == 302


@pytest.mark.django_db
def test_meal_update_view(client, user, meal):
    client.login(username="testuser", password="testpassword")
    response = client.get(
        reverse("tools:meal_update", args=[meal.id])
    )
    assert response.status_code == 302


@pytest.mark.django_db
def test_meal_delete_view(client, user, meal):
    client.login(username="testuser", password="testpassword")
    response = client.get(
        reverse("tools:meal_delete", args=[meal.id])
    )
    assert response.status_code == 302


@pytest.mark.django_db
def test_meal_detail_view(client, user, meal):
    client.login(username="testuser", password="testpassword")
    response = client.get(reverse("tools:meal_details", args=[meal.id]))
    assert response.status_code == 302


@pytest.mark.django_db
def test_meal_daily_plan_create_view(client, user):
    client.login(username="testuser", password="testpassword")
    response = client.get(reverse("tools:meal_plan_create"))
    assert response.status_code == 302


@pytest.mark.django_db
def test_meal_daily_plan_update_view(client, user, meal_daily_plan):
    client.login(username="testuser", password="testpassword")
    response = client.get(reverse("tools:meal_plan_update", args=[meal_daily_plan.id]))
    assert response.status_code == 302


@pytest.mark.django_db
def test_meal_daily_plan_delete_view(client, user, meal_daily_plan):
    client.login(username="testuser", password="testpassword")
    response = client.get(reverse("tools:meal_plan_delete", args=[meal_daily_plan.id]))
    assert response.status_code == 302


@pytest.mark.django_db
def test_meal_daily_plan_detail_view(client, user, meal_daily_plan):
    client.login(username="testuser", password="testpassword")
    response = client.get(reverse("tools:meal_plan_details", args=[meal_daily_plan.id]))
    assert response.status_code == 302
