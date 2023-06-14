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
    Quantity
)


@admin.register(Type)
class TypeAdmin(admin.ModelAdmin):
    list_display = ["name"]

    list_filter = ["name"]


@admin.register(Quantity)
class QuantityAdmin(admin.TabularInline):
    list_display = ["name", "value"]

    list_filter = ["name", "value"]


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
    list_display = ["value"]

    list_filter = ["value"]


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
        "meat",
        "vegetarian",
        "vegan",
        "country",
        "level",
        "category",
    ]
