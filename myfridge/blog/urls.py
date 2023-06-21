from django.urls import path
from . import views

app_name = "blog"


urlpatterns = [
    path("post/create/", views.PostCreateView.as_view(), name="create_post"),
    path("post/update/<int:pk>/", views.PostUpdateView.as_view(), name="update_post"),
    path("post/delete/<int:pk>/", views.PostDeleteView.as_view(), name="delete_post"),
    path("", views.PostListView.as_view(), name="post_list"),
    path("post/<int:pk>/", views.PostDetailView.as_view(), name="post_detail"),
    path(
        "comment/create/<int:post_id>/",
        views.CommentCreateView.as_view(),
        name="create_comment",
    ),
    path(
        "comment/update/<int:pk>/",
        views.CommentUpdateView.as_view(),
        name="update_comment",
    ),
    path(
        "comment/delete/<int:pk>/",
        views.CommentDeleteView.as_view(),
        name="delete_comment",
    ),
]
