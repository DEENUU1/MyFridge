from django.contrib import admin
from .models import Rate, Feedback


class RateInline(admin.TabularInline):
    model = Rate


@admin.register(Rate)
class RateAdmin(admin.ModelAdmin):
    list_display = ["dish", "author", "choose_rate", "date_created"]

    list_filter = ["author", "date_created", "choose_rate"]


@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ["message", "date_created"]

    list_filter = ["date_created"]
