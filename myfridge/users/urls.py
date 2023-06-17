from django.urls import path
from . import views

app_name = "users"


urlpatterns = [
    path("register/", views.RegisterUserView.as_view(), name="register"),
    path(
        "activate/<str:uidb64>/<str:token>/", views.send_activation_url, name="activate"
    ),
    path(
        "register/success", views.SuccessRegisterView.as_view(), name="success_register"
    ),
    path("login/", views.LoginUserView.as_view(), name="login"),
    path("logout/", views.LogoutUserView.as_view(), name="logout"),
    path("statute/", views.StatuteView.as_view(), name="statute"),
    path(
        "change_password/", views.ChangePasswordView.as_view(), name="change_password"
    ),
    path(
        "change_password_success/",
        views.SuccessPasswordChangeView.as_view(),
        name="success_password_change",
    ),
    path("delete_account/", views.DeleteAccountView.as_view(), name="delete_account"),
    path(
        "delete_account_success/",
        views.SuccessDeleteAccountView.as_view(),
        name="success_delete_account",
    ),
    path("profile/", views.UserProfileView.as_view(), name="profile"),
    path(
        "profile/update/<int:pk>/",
        views.UpdateProfileView.as_view(),
        name="edit_profile",
    ),
    path("post/create/", views.PostCreateView.as_view(), name="create_post"),
    path("post/update/<int:pk>/", views.PostUpdateView.as_view(), name="update_post"),
    path("post/delete/<int:pk>/", views.PostDeleteView.as_view(), name="delete_post"),
    path("post/list/", views.PostListView.as_view(), name="post_list"),
    path("post/<int:pk>/", views.PostDetailView.as_view(), name="post_detail"),
    path("comment/create/", views.CommentCreateView.as_view(), name="create_comment"),
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
