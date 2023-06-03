from django.urls import path
from . import views

app_name = "dishes"


urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),
    path("dish/<int:pk>/", views.DishDetailView.as_view(), name="dish-detail"),
    path("dish/create/", views.DishCreateView.as_view(), name="dish-create"),
    path("dish/<int:pk>/delete", views.DeleteDishView.as_view(), name="dish-delete"),
    path("dish/<int:pk>/update", views.UpdateDishView.as_view(), name="dish-update"),
]
