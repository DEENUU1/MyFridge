from django.contrib import admin
from .models import Rate


class RateInline(admin.TabularInline):
    model = Rate


@admin.register(Rate)
class RateAdmin(admin.ModelAdmin):
    list_display = ["dish", "author", "choose_rate", "date_created"]

    list_filter = ["author", "date_created", "choose_rate"]
