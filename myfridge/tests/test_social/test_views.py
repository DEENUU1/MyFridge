import pytest
from django.urls import reverse
from django.test import Client
from django.shortcuts import get_object_or_404
from social.models import Rate, FavouriteDish
from dishes.models import (
    Dish,
    TimeToMake,
    Country,
    DishCategory,
    DifficultyLevel,
    Type,
    MainIngredient,
    OtherIngredient,
    CustomUser,
)
from users.models import CustomUser as User


@pytest.fixture
def client():
    return Client()


@pytest.fixture
def user():
    return User.objects.create_user(username="testuser", password="testpassword")


@pytest.fixture
def dish(user):
    time_to_make = TimeToMake.objects.create(value=30)
    country = Country.objects.create(name="Italy")
    level = DifficultyLevel.objects.create(name="Easy")
    category = DishCategory.objects.create(name="Main Course")
    type = Type.objects.create(name="Ingredient")
    main_ingredient = MainIngredient.objects.create(name="Tomato", type=type)
    other_ingredient = OtherIngredient.objects.create(name="Garlic", type=type)
    user = user

    dish = Dish.objects.create(
        name="Pasta",
        author=user,
        time_to_make=time_to_make,
        description="Delicious pasta dish",
        kcal=500,
        gluten=True,
        lactose=False,
        meat=True,
        vegetarian=True,
        vegan=False,
        country=country,
        level=level,
        category=category,
    )
    dish.main_ingredient.add(main_ingredient)
    dish.other_ingredients.add(other_ingredient)

    return dish


@pytest.mark.django_db
def test_create_rate_view(client, user, dish):
    client.login(username="testuser", password="testpassword")

    response = client.post(
        reverse("social:rate-add", kwargs={"pk": dish.pk}),
        {"choose_rate": 5, "comment": "Test comment"},
    )

    assert response.status_code == 200


@pytest.mark.django_db
def test_update_rate_view(client, user, dish):
    rate = Rate.objects.create(
        choose_rate=3, comment="Initial comment", dish=dish, author=user
    )

    client.login(username="testuser", password="testpassword")

    response = client.post(
        reverse("social:rate-update", kwargs={"pk": rate.pk}),
        {"choose_rate": 4, "comment": "Updated comment"},
    )

    assert response.status_code == 302
    rate.refresh_from_db()
    assert rate.choose_rate == 4
    assert rate.comment == "Updated comment"


@pytest.mark.django_db
def test_delete_rate_view(client, user, dish):
    rate = Rate.objects.create(
        choose_rate=3, comment="Test comment", dish=dish, author=user
    )

    client.login(username="testuser", password="testpassword")

    response = client.post(reverse("social:rate-delete", kwargs={"pk": rate.pk}))

    assert response.status_code == 302
    assert not Rate.objects.filter(pk=rate.pk).exists()


@pytest.mark.django_db
def test_add_to_favourites_view(client, user, dish):
    client.login(username="testuser", password="testpassword")

    response = client.post(reverse("social:favourite-add", kwargs={"dish_id": dish.pk}))

    assert response.status_code == 302


@pytest.mark.django_db
def test_delete_from_favourites_view(client, user, dish):
    favourite_dish = FavouriteDish.objects.create(user=user, dish=dish)

    client.login(username="testuser", password="testpassword")

    response = client.post(
        reverse("social:favourite-remove", kwargs={"favourite_id": favourite_dish.pk})
    )

    response.status_code == 302
    assert not FavouriteDish.objects.filter(pk=favourite_dish.pk).exists()


@pytest.mark.django_db
def test_user_ranking_view(client):
    response = client.get(reverse("social:user-ranking"))
    assert response.status_code == 200


@pytest.mark.django_db
def test_create_rate_view_unauthenticated(client, dish):
    response = client.post(
        reverse("social:rate-add", kwargs={"pk": dish.pk}),
        {"choose_rate": 5, "comment": "Test comment"},
    )
    assert response.status_code == 302
    assert response.url.startswith(reverse("users:login"))
