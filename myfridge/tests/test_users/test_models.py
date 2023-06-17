import pytest
from users.models import CustomUser
from test_data.models_fixtures import user
from users.models import Post, Comment


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
def test_model_post_successfully_created(user):
    post = Post.objects.create(
        title="Test post",
        text="Test post text",
        author=user,
    )
    assert post.title == "Test post"
    assert post.text == "Test post text"
    assert post.author == user
    assert post.__str__() == "Test post"


@pytest.mark.django_db
def test_model_comment_successfully_created(user):
    post = Post.objects.create(
        title="Test post",
        text="Test post text",
        author=user,
    )
    comment = Comment.objects.create(
        text="Test comment",
        author=user,
        post=post,
    )
    assert comment.text == "Test comment"
    assert comment.author == user
    assert comment.post == post
    assert comment.__str__() == f"{user} {post}"
