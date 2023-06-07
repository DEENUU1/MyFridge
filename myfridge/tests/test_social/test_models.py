import pytest
from social.models import Rate, Feedback, FavouriteDish
from users.models import CustomUser
from dishes.models import (
    Dish,
    TimeToMake,
    Country,
    DifficultyLevel,
    DishCategory,
    Type,
    MainIngredient,
    OtherIngredient,
)


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


@pytest.mark.django_db
def test_model_rate_successfully_created(dish_data):
    user = CustomUser.objects.create(username="anotheruser", password="testpassword")
    rate = Rate.objects.create(
        choose_rate=5,
        comment="Great dish!",
        dish=dish_data,
        author=user,
    )

    assert isinstance(rate, Rate)
    assert rate.choose_rate == 5
    assert rate.comment == "Great dish!"
    assert rate.dish == dish_data
    assert rate.author.username == "anotheruser"
    assert rate.__str__() == "Pasta 5"


@pytest.mark.django_db
def test_model_feedback_successfully_created(dish_data):
    feedback = Feedback.objects.create(message="I dont need that website anymore!")
    assert feedback.message == "I dont need that website anymore!"
    assert len(feedback.__str__()) == 15


@pytest.mark.django_db
def test_model_favourite_dish_successfully_created(dish_data):
    user = CustomUser.objects.create(username="test_user", password="testpassword")
    favourite_dish = FavouriteDish.objects.create(dish=dish_data, user=user)

    assert isinstance(favourite_dish, FavouriteDish)
    assert favourite_dish.dish == dish_data
    assert favourite_dish.user.username == "test_user"
    assert favourite_dish.__str__() == "test_user Pasta"
