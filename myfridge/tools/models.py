from django.db import models
from users.models import CustomUser
from dishes.models import Dish


class ShoppingList(models.Model):
    name = models.CharField(max_length=200)
    date_created = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    is_bought = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Meal(models.Model):
    name = models.CharField(max_length=200)
    content = models.TextField(null=True)
    url = models.URLField(null=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name
