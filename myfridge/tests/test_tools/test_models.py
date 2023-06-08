import pytest
from django.contrib.auth import get_user_model
from tools.models import ShoppingList
from test_data.models_fixtures import user 


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
