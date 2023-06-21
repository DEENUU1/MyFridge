from django.contrib import admin
from .models import Comment, Post


@admin.register(Post)
class PostModelAdmin(admin.ModelAdmin):
    list_display = ["title", "author", "created_date", "updated_date"]
    list_filter = ["author", "created_date", "updated_date"]


@admin.register(Comment)
class CommentModelAdmin(admin.ModelAdmin):
    list_display = ["author", "post", "date_created", "date_updated"]
    list_filter = ["author", "date_created", "date_updated"]
