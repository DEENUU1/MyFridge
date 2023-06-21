import pytest
from users.models import CustomUser, UserFollowing
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


@pytest.mark.django_db
def test_model_user_following_successfully_created():
    user_1 = CustomUser.objects.create_user(
        username="test user",
        email="test@example.com",
        password="Str0ngPassword1",
        description="Simple test description",
    )
    user_2 = CustomUser.objects.create_user(
        username="test user2",
        email="test2@example.com",
        password="Str0ngPassword1",
        description="Simple test description",
    )
    user_following = UserFollowing.objects.create(
        user_id=user_1, following_user_id=user_2
    )
    assert user_following.user_id == user_1
    assert user_following.following_user_id == user_2
    assert user_following.__str__() == f"{user_1} is following {user_2}"
