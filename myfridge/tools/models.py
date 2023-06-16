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


class MealDailyPlan(models.Model):
    MONTHS = ((1, "January"),
              (2, "February"),
              (3, "March"),
              (4, "April"),
              (5, "May"),
              (6, "June"),
              (7, "July"),
              (8, "August"),
              (9, "September"),
              (10, "October"),
              (11, "November"),
              (12, "December"))

    YEARS = ((4,  "2023"),
             (5,  "2024"),
             (6,  "2025"),)

    date = models.DateField()
    month = models.IntegerChoices(MONTHS)
    year = models.IntegerField(YEARS)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    breakfast = models.ForeignKey(Meal, on_delete=models.CASCADE, related_name='breakfast', null=True)
    second_breakfast = models.ForeignKey(Meal, on_delete=models.CASCADE, related_name='second_breakfact', null=True)
    lunch = models.ForeignKey(Meal, on_delete=models.CASCADE, related_name="lunch", null=True)
    tea = models.ForeignKey(Meal, on_delete=models.CASCADE, related_name="tea", null=True)
    dinner = models.ForeignKey(Meal, on_delete=models.CASCADE, related_name="dinner", null=True)

    def __str__(self):
        return f"{self.date} {self.month} {self.year}"
