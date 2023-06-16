from dishes.models import (
    Type,
    Country,
    MainIngredient,
    OtherIngredient,
    DifficultyLevel,
    DishCategory,
    TimeToMake,
    Dish,
    Quantity,
)
from test_data.models_fixtures import dish_data

import pytest


@pytest.mark.django_db
def test_model_type_successfully_created():
    type_obj = Type.objects.create(name="Milk")
    assert type_obj.name == "Milk"
    assert type_obj.__str__() == "Milk"


@pytest.mark.django_db
def test_model_country_successfully_created():
    country = Country.objects.create(name="Poland")
    assert country.name == "Poland"
    assert country.__str__() == "Poland"


@pytest.mark.django_db
def test_model_main_ingredient_successfully_created():
    main_ingredient = MainIngredient.objects.create(
        name="Cheese", type=Type.objects.create(name="Milk")
    )
    assert main_ingredient.name == "Cheese"
    assert main_ingredient.type.name == "Milk"
    assert main_ingredient.__str__() == "Cheese"


@pytest.mark.django_db
def test_model_other_ingredient_successfully_created():
    other_ingredient = OtherIngredient.objects.create(
        name="Paper", type=Type.objects.create(name="Seasoning")
    )
    assert other_ingredient.name == "Paper"
    assert other_ingredient.type.name == "Seasoning"
    assert other_ingredient.__str__() == "Paper"


@pytest.mark.django_db
def test_model_difficulty_level_successfully_created():
    difficulty_level = DifficultyLevel.objects.create(name="Easy")
    assert difficulty_level.name == "Easy"
    assert difficulty_level.__str__() == "Easy"


@pytest.mark.django_db
def test_model_dish_category_successfully_created():
    dish_category = DishCategory.objects.create(name="Breakfast")
    assert dish_category.name == "Breakfast"
    assert dish_category.__str__() == "Breakfast"


@pytest.mark.django_db
def test_model_time_to_make_successfully_created():
    time_to_make = TimeToMake.objects.create(value=30)
    assert time_to_make.__str__() == "30"


@pytest.mark.django_db
def test_model_quantity_successfully_created():
    quantity = Quantity.objects.create(value=1, unit="gram")
    assert quantity.__str__() == "1 gram"


@pytest.mark.django_db
def test_model_dish_successfully_created(dish_data):
    assert isinstance(dish_data, Dish)
    assert dish_data.name == "Pasta"
    assert dish_data.author.username == "testuser"
    assert dish_data.time_to_make.get_values == "30 minutes"
    assert dish_data.description == "Delicious pasta dish"
    assert dish_data.kcal == 500
    assert dish_data.gluten is True
    assert dish_data.lactose is False
    assert dish_data.meat is True
    assert dish_data.vegetarian is True
    assert dish_data.vegan is False
    assert dish_data.country.name == "Italy"
    assert dish_data.level.name == "Easy"
    assert dish_data.main_ingredient.count() == 1
    assert dish_data.other_ingredients.count() == 1
    assert dish_data.category.name == "Main Course"
    assert dish_data.__str__() == "Pasta"
