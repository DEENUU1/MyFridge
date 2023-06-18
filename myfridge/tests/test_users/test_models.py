import pytest
from users.models import CustomUser
from test_data.models_fixtures import user


@pytest.mark.django_db
def test_model_custom_user_successfully_created():
    user = CustomUser.objects.create_user(
        username="test user",
        email="test@example.com",
        password="Str0ngPassword1",
        description="Simple test description",
    )
    assert user.username == "test user"
    assert user.email == "test@example.com"
    assert user.description == "Simple test description"
    assert user.points == 0
