from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    description = models.CharField(max_length=200, default=None, blank=True, null=True)
    image = models.ImageField(upload_to="images", default=None, blank=True, null=True)
    points = models.IntegerField(default=0)
