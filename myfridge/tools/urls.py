from django.urls import path
from . import views

app_name = "tools"


urlpatterns = [
    path("bmi/", views.bmiView, name="bmi"),
    path("shopping_list/", views.ShoppingListView.as_view(), name="shopping_list"),
    path(
        "shopping_list/create/",
        views.ShoppingListCreateView.as_view(),
        name="shopping_list_create",
    ),
    path(
        "shopping_list/update/<int:pk>/",
        views.ShoppingListUpdateView.as_view(),
        name="shopping_list_update",
    ),
    path(
        "shopping_list/delete/<int:pk>/",
        views.ShoppingListDeleteView.as_view(),
        name="shopping_list_delete",
    ),
]
