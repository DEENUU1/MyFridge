from django.contrib import admin
from .models import CustomUser


@admin.register(CustomUser)
class UserModelAdmin(admin.ModelAdmin):
    list_display = [
        "username",
        "email",
        "points",
        "is_active",
    ]

    list_filter = ["is_active", "points"]