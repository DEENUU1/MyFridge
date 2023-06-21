from django.urls import reverse
from django.test import RequestFactory
from test_data.models_fixtures import factory, user, client, user_inactive
import pytest
from blog.models import Post, Comment
from blog.views import (
    PostCreateView,
    PostDeleteView,
    PostDetailView,
    PostListView,
    PostUpdateView,
    CommentCreateView,
    CommentDeleteView,
    CommentUpdateView,
)


@pytest.fixture
def post(user):
    return Post.objects.create(author=user, title="test title", text="test text")


@pytest.fixture
def comment(user, post):
    return Comment.objects.create(author=user, text="test text", post=post)


@pytest.mark.django_db
def test_post_create_view(user, factory):
    request = factory.get(reverse("blog:create_post"))
    request.user = user

    response = PostCreateView.as_view()(request)

    assert response.status_code == 200


# @pytest.mark.django_db
# def test_post_update_view(user, post, factory):
#     request = factory.get(reverse("blog:update_post", kwargs={"pk": post.pk}))
#     request.user = user
#
#     response = PostUpdateView.as_view()(request, pk=post.pk)
#
#     assert response.status_code == 200


# @pytest.mark.django_db
# def test_post_delete_view(user, post, factory):
#     request = factory.get(reverse("blog:delete_post", kwargs={"pk": post.pk}))
#     request.user = user
#
#     response = PostDeleteView.as_view()(request, pk=post.pk)
#
#     assert response.status_code == 200


@pytest.mark.django_db
def test_post_list_view(user, factory):
    request = factory.get(reverse("blog:post_list"))
    request.user = user

    response = PostListView.as_view()(request)

    assert response.status_code == 200


@pytest.mark.django_db
def test_post_detail_view(user, post, factory):
    request = factory.get(reverse("blog:post_detail", kwargs={"pk": post.pk}))
    request.user = user

    response = PostDetailView.as_view()(request, pk=post.pk)

    assert response.status_code == 200


@pytest.mark.django_db
def test_comment_create_view(user, factory, post):
    request = factory.get(reverse("blog:create_comment", kwargs={"post_id": post.pk}))
    request.user = user

    response = CommentCreateView.as_view()(request)

    assert response.status_code == 200


# @pytest.mark.django_db
# def test_comment_update_view(user, comment, factory):
#     request = factory.get(reverse("blog:update_comment", kwargs={"pk": comment.pk}))
#     request.user = user
#
#     response = CommentUpdateView.as_view()(request, pk=comment.pk)
#
#     assert response.status_code == 200


# @pytest.mark.django_db
# def test_comment_delete_view(user, comment, factory):
#     request = factory.get(reverse("blog:delete_comment", kwargs={"pk": comment.pk}))
#     request.user = user
#
#     response = CommentDeleteView.as_view()(request, pk=comment.pk)
#
#     assert response.status_code == 200
