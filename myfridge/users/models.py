from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    description = models.CharField(max_length=200, default=None, blank=True, null=True)
    image = models.ImageField(upload_to="images", default=None, blank=True, null=True)
    newsletter = models.BooleanField(default=False)
    points = models.IntegerField(default=0)


class Post(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    image = models.ImageField(upload_to="images", default=None, blank=True, null=True)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    text = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.author} {self.post}"
