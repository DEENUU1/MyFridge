import pytest
from django.contrib.auth import get_user_model
from tools.models import ShoppingList, Meal, MealDailyPlan
from test_data.models_fixtures import dish_data
from django.utils import timezone
from users.models import CustomUser


@pytest.mark.django_db
def test_model_shopping_list_successfully_created(user):
    shopping_list = ShoppingList.objects.create(
        name="Test Shopping List",
        author=user,
        quantity=1,
        is_bought=False,
    )
    assert shopping_list.name == "Test Shopping List"
    assert shopping_list.author == user
    assert shopping_list.quantity == 1
    assert shopping_list.is_bought == False
    assert shopping_list.__str__() == "Test Shopping List"


@pytest.fixture
def user():
    return CustomUser.objects.create(username="testuser123", password="testpass123")


@pytest.fixture
def meal(user, dish_data):
    return Meal.objects.create(name="testmeal", user=user, dish=dish_data)


@pytest.mark.django_db
def test_meal_daily_plan(user, meal):
    meal_daily_plan = MealDailyPlan.objects.create(
        date=timezone.now().date(),
        month="June",
        year="2023",
        user=user,
        breakfast=meal,
        second_breakfast=meal,
        lunch=meal,
        tea=meal,
        dinner=meal,
    )

    retrieved_plan = MealDailyPlan.objects.get(id=meal_daily_plan.id)

    assert retrieved_plan.date == meal_daily_plan.date
    assert retrieved_plan.month == meal_daily_plan.month
    assert retrieved_plan.year == meal_daily_plan.year
    assert retrieved_plan.breakfast == meal_daily_plan.breakfast
    assert retrieved_plan.second_breakfast == meal_daily_plan.second_breakfast
    assert retrieved_plan.lunch == meal_daily_plan.lunch
    assert retrieved_plan.tea == meal_daily_plan.tea
    assert retrieved_plan.dinner == meal_daily_plan.dinner
