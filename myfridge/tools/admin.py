from django.contrib import admin
from .models import ShoppingList


@admin.register(ShoppingList)
class RateAdmin(admin.ModelAdmin):
    list_display = ["name", "date_created", "author", "quantity", "is_bought"]

    list_filter = ["date_created", "is_bought", "author"]
