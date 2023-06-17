from contact.views import ContactSuccessView, ContactStatueView
from django.urls import reverse
from django.test import RequestFactory
from test_data.models_fixtures import factory, user, client, user_inactive
import pytest
from users.models import Post, Comment
from users.views import (
    PostCreateView,
    PostDeleteView,
    PostDetailView,
    PostListView,
    PostUpdateView,
    CommentCreateView,
    CommentDeleteView,
    CommentUpdateView,
)


def test_users_success_register_view_get_method_returns_200_status_code(factory):
    request = factory.get(reverse("users:success_register"))
    view = ContactSuccessView.as_view(template_name="success_register.html")
    response = view(request)
    assert response.status_code == 200


def test_users_statute_view_get_method_returns_200_status_code(factory):
    request = factory.get(reverse("users:statute"))
    view = ContactSuccessView.as_view(template_name="statute.html")
    response = view(request)
    assert response.status_code == 200


def test_users_success_password_change_view_get_method_returns_200_status_code(factory):
    request = factory.get(reverse("users:success_password_change"))
    view = ContactSuccessView.as_view(template_name="password_change_success.html")
    response = view(request)
    assert response.status_code == 200


@pytest.mark.django_db
def test_register_view(client):
    response = client.get(reverse("users:register"))
    assert response.status_code == 200


@pytest.mark.django_db
def test_success_register_view(client):
    response = client.get(reverse("users:success_register"))
    assert response.status_code == 200


@pytest.mark.django_db
def test_login_view(client, user):
    response = client.post(
        reverse("users:login"), {"username": "testuser", "password": "12345"}
    )
    assert response.status_code == 200


@pytest.mark.django_db
def test_logout_view(client, user):
    client.login(username="testuser", password="12345")
    response = client.get(reverse("users:logout"))
    assert response.status_code == 302  # It should redirect after logout


@pytest.mark.django_db
def test_statute_view(client):
    response = client.get(reverse("users:statute"))
    assert response.status_code == 200


@pytest.mark.django_db
def test_change_password_view(client, user):
    client.login(username="testuser", password="12345")
    response = client.get(reverse("users:change_password"))
    assert response.status_code == 200


@pytest.mark.django_db
def test_success_password_change_view(client):
    response = client.get(reverse("users:success_password_change"))
    assert response.status_code == 200


@pytest.mark.django_db
def test_delete_account_view(client, user):
    client.login(username="testuser", password="12345")
    response = client.get(reverse("users:delete_account"))
    assert response.status_code == 200


@pytest.mark.django_db
def test_success_delete_account_view(client):
    response = client.get(reverse("users:success_delete_account"))
    assert response.status_code == 200


@pytest.mark.django_db
def test_user_profile_view(client, user):
    client.login(username="testuser", password="12345")
    response = client.get(reverse("users:profile"))
    assert response.status_code == 302


@pytest.mark.django_db
def test_update_profile_view(client, user):
    client.login(username="testuser", password="12345")
    response = client.get(reverse("users:edit_profile", kwargs={"pk": user.pk}))
    assert response.status_code == 302


@pytest.fixture
def post(user):
    return Post.objects.create(author=user, title="test title", text="test text")


@pytest.fixture
def comment(user, post):
    return Comment.objects.create(author=user, text="test text", post=post)


@pytest.mark.django_db
def test_post_create_view(user, factory):
    request = factory.get(reverse("users:create_post"))
    request.user = user

    response = PostCreateView.as_view()(request)

    assert response.status_code == 200


@pytest.mark.django_db
def test_post_update_view(user, post, factory):
    request = factory.get(reverse("users:update_post", kwargs={"pk": post.pk}))
    request.user = user

    response = PostUpdateView.as_view()(request, pk=post.pk)

    assert response.status_code == 200


@pytest.mark.django_db
def test_post_delete_view(user, post, factory):
    request = factory.get(reverse("users:delete_post", kwargs={"pk": post.pk}))
    request.user = user

    response = PostDeleteView.as_view()(request, pk=post.pk)

    assert response.status_code == 200


@pytest.mark.django_db
def test_post_list_view(user, factory):
    request = factory.get(reverse("users:post_list"))
    request.user = user

    response = PostListView.as_view()(request)

    assert response.status_code == 200


@pytest.mark.django_db
def test_post_detail_view(user, post, factory):
    request = factory.get(reverse("users:post_detail", kwargs={"pk": post.pk}))
    request.user = user

    response = PostDetailView.as_view()(request, pk=post.pk)

    assert response.status_code == 200


@pytest.mark.django_db
def test_comment_create_view(user, factory):
    request = factory.get(reverse("users:create_comment"))
    request.user = user

    response = CommentCreateView.as_view()(request)

    assert response.status_code == 200


@pytest.mark.django_db
def test_comment_update_view(user, comment, factory):
    request = factory.get(reverse("users:update_comment", kwargs={"pk": comment.pk}))
    request.user = user

    response = CommentUpdateView.as_view()(request, pk=comment.pk)

    assert response.status_code == 200


@pytest.mark.django_db
def test_comment_delete_view(user, comment, factory):
    request = factory.get(reverse("users:delete_comment", kwargs={"pk": comment.pk}))
    request.user = user

    response = CommentDeleteView.as_view()(request, pk=comment.pk)

    assert response.status_code == 200
