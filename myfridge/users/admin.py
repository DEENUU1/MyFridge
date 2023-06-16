from django.contrib import admin
from .models import CustomUser, Points


@admin.register(CustomUser)
class UserModelAdmin(admin.ModelAdmin):
    list_display = [
        "username",
        "email",
        "is_active",
    ]

    list_filter = ["is_active"]


@admin.register(Points)
class PointsModelAdmin(admin.ModelAdmin):
    list_display = ["user", "points"]
    list_filter = ["user", "points"]