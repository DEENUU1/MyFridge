from django.contrib import admin
from .models import ShoppingList, Meal, MealDailyPlan, UserStatistics


@admin.register(ShoppingList)
class RateAdmin(admin.ModelAdmin):
    list_display = ["name", "date_created", "author", "quantity", "is_bought"]

    list_filter = ["date_created", "is_bought", "author"]


@admin.register(Meal)
class MealModelAdmin(admin.ModelAdmin):
    list_display = ["name", "user"]
    list_filter = ["user"]


@admin.register(MealDailyPlan)
class MealDailyPlanModelAdmin(admin.ModelAdmin):
    list_display = ["date", "month", "year", "user"]
    list_filter = ["date", "month", "year", "user"]


@admin.register(UserStatistics)
class UserStatisticsModelAdmin(admin.ModelAdmin):
    list_display = [
        "user",
        "current_weight",
        "dream_weight",
        "current_height",
        "date_created",
        "date_updated",
    ]
    list_filter = ["user", "date_created", "date_updated"]
