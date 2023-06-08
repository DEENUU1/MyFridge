import datetime
import pytest 
from users.models import CustomUser
from django.test import RequestFactory
from dishes.models import (
    TimeToMake,
    Country,
    DifficultyLevel,
    DishCategory,
    Type,
    MainIngredient,
    OtherIngredient,
    Dish
)
from fak.models import Fak, Medicine


@pytest.fixture
def user():
    return CustomUser.objects.create_user(username="testuser", password="testpass")


@pytest.fixture
def factory():
    return RequestFactory()

@pytest.fixture
def dish_data():
    time_to_make = TimeToMake.objects.create(value=30)
    country = Country.objects.create(name="Italy")
    level = DifficultyLevel.objects.create(name="Easy")
    category = DishCategory.objects.create(name="Main Course")
    type = Type.objects.create(name="Ingredient")
    main_ingredient = MainIngredient.objects.create(name="Tomato", type=type)
    other_ingredient = OtherIngredient.objects.create(name="Garlic", type=type)
    user = CustomUser.objects.create(username="testuser", password="testpassword")

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

@pytest.fixture
def fak(user):
    return Fak.objects.create(name="Test Fak", author=user)


@pytest.fixture
def medicine(fak, user):
    return Medicine.objects.create(
        name="Test Medicine",
        expiration_date=datetime.date.today() + datetime.timedelta(days=7),
        quantity="MEDIUM",
        fak=fak,
        author=user,
    )
