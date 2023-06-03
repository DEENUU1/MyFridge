from django.contrib import admin

from .models import (
    Type,
    Country,
    MainIngredient,
    OtherIngredient,
    DifficultyLevel,
    DishCategory,
    TimeToMake,
    Dish,
    Rate,
)


@admin.register(Type)
class TypeAdmin(admin.ModelAdmin):
    list_display = ["name"]

    list_filter = ["name"]


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ["name"]

    list_filter = ["name"]


@admin.register(MainIngredient)
class MainIngredientAdmin(admin.ModelAdmin):
    list_display = ["name", "type"]

    list_filter = ["name", "type"]


@admin.register(OtherIngredient)
class OtherIngredientAdmin(admin.ModelAdmin):
    list_display = ["name", "type"]

    list_filter = ["name", "type"]


@admin.register(DifficultyLevel)
class DifficultyLevelAdmin(admin.ModelAdmin):
    list_display = ["name"]

    list_filter = ["name"]


@admin.register(DishCategory)
class DishCategoryAdmin(admin.ModelAdmin):
    list_display = ["name"]

    list_filter = ["name"]


@admin.register(TimeToMake)
class TimeToMakeAdmin(admin.ModelAdmin):
    list_display = ["time", "name"]

    list_filter = ["time", "name"]


@admin.register(Dish)
class DishAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "author",
        "date_created",
        "date_edited",
        "time_to_make",
        "category",
        "level",
        "country",
    ]

    list_filter = [
        "author",
        "date_created",
        "date_edited",
        "time_to_make",
        "kcal",
        "gluten",
        "lactose",
        "meal",
        "vegetarian",
        "vegan",
        "country",
        "level",
        "category",
    ]


class RateInline(admin.TabularInline):
    model = Rate


@admin.register(Rate)
class RateAdmin(admin.ModelAdmin):
    list_display = ["dish", "author", "choose_rate", "date_created"]

    list_filter = ["author", "date_created", "choose_rate"]
