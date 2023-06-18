from django.contrib import admin
from .models import CustomUser, UserFollowing


@admin.register(CustomUser)
class UserModelAdmin(admin.ModelAdmin):
    list_display = ["username", "email", "is_active", "points"]

    list_filter = ["is_active"]


@admin.register(UserFollowing)
class UserFollowingAdmin(admin.ModelAdmin):
    list_display = ["user_id", "following_user_id"]