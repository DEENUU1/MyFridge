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
    path("caloric-needs/", views.caloricNeedsView, name="caloric-needs"),
    path("perfect-weight/", views.perfect_weight_view, name="perfect-weight"),
    path("meal/create", views.MealCreateView.as_view(), name="meal_create"),
    path("meal/update/<int:pk>", views.MealUpdateView.as_view(), name="meal_update"),
    path("meal/delete/<int:pk>", views.MealDeleteView.as_view(), name="meal_delete"),
    path("meal/details/<int:pk>", views.MealDetailView.as_view(), name="meal_details"),
    path("meal-plan/create", views.MealDailyPlanCreateView.as_view(), name="meal_plan_create"),
    path("meal-plan/update/<int:pk>", views.MealDailyPlanUpdateView.as_view(), name="meal_plan_update"),
    path("meal-plan/delete/<int:pk>", views.MealDailyPlanDeleteView.as_view(), name="meal_plan_delete"),
    path("meal-plan/details/<int:pk>", views.MealDailyPlanDetailView.as_view(), name="meal_plan_details"),
    path("meal-plan/list", views.MealDailyPlanListView.as_view(), name="meal_plan_list"),

]
