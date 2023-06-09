from django.urls import path
from . import views

app_name = "social"


urlpatterns = [
    path("dish/<int:pk>/rate-add", views.CreateRateView.as_view(), name="rate-add"),
    path("rate/<int:pk>/update", views.UpdateRateView.as_view(), name="rate-update"),
    path("rate/<int:pk>/delete", views.DeleteRateView.as_view(), name="rate-delete"),
    path("rate/ranking", views.UserRankingView.as_view(), name="user-ranking"),
    path(
        "favourites/add/<int:dish_id>",
        views.AddToFavouritesView.as_view(),
        name="favourite-add",
    ),
    path(
        "favourites/remove/<int:favourite_id>",
        views.DeleteFromFavouriteView.as_view(),
        name="favourite-remove",
    ),
]
