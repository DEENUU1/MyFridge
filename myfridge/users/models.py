from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    description = models.CharField(max_length=200, default=None, blank=True, null=True)
    image = models.ImageField(upload_to="images", default=None, blank=True, null=True)
    newsletter = models.BooleanField(default=False)


class Points(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    points = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.user.username} - {self.points}"