import pytest
from test_data.models_fixtures import user
from blog.models import Post, Comment


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
