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
from django.test import Client
from tools.models import ShoppingList

@pytest.fixture
def user():
    return CustomUser.objects.create_user(username="testuser", password="testpass")

@pytest.fixture
def user_inactive():
    user = CustomUser.objects.create_user(username='testuser_inactive', password='12345')
    user.is_active = False
    user.save()
    return user

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
def client():
    return Client()

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

@pytest.fixture
def authenticated_user(db):
    user = CustomUser.objects.create_user(username='testuser', password='12345')
    return user

@pytest.fixture
def client_with_authenticated_user(db, authenticated_user):
    client = Client()
    client.login(username=authenticated_user.username, password='12345')
    return client

@pytest.fixture
def shopping_list(db, authenticated_user):
    return ShoppingList.objects.create(name='test', author=authenticated_user, quantity=5)

@pytest.fixture
def bmi_form_data():
    return {'weight': 70, 'height': 170}