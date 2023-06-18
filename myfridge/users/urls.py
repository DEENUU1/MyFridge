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
    path("profile/<int:pk>/detail", views.ProfileDetailView.as_view(), name="profile_detail"),
    path("follow/<int:pk>/", views.FollowUserView.as_view(), name="follow"),
    path("unfollow/<int:pk>/", views.UnfollowUserView.as_view(), name="unfollow"),
    path("profile/<int:pk/following", views.UserFollowersListView.as_view(), name="following"),
    path("profile/<int:pk/followers", views.UserFollowersListView.as_view(), name="followers"),
]
