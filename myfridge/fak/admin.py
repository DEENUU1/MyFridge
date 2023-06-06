from django.contrib import admin
from .models import Fak, Medicine


@admin.register(Fak)
class RateAdmin(admin.ModelAdmin):
    list_display = ["name"]

    list_filter = ["name"]


@admin.register(Medicine)
class RateAdmin(admin.ModelAdmin):
    list_display = ["name", "quantity", "fak", "expiration_date"]

    list_filter = ["name", "expiration_date", "fak", "quantity"]
