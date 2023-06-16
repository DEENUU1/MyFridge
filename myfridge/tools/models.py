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
    content = models.TextField(null=True, blank=True)
    url = models.URLField(null=True, blank=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name


class MealDailyPlan(models.Model):
    MONTHS = (("January", "January"),
              ("February", "February"),
              ("March", "March"),
              ("April", "April"),
              ("May", "May"),
              ("June", "June"),
              ("July", "July"),
              ("August", "August"),
              ("September", "September"),
              ("October", "October"),
              ("November", "November"),
              ("December", "December"),)

    YEARS = (("2023",  "2023"),
             ("2024",  "2024"),
             ("2025",  "2025"),)

    date = models.DateField()
    month = models.CharField(max_length=20, choices=MONTHS)
    year = models.CharField(max_length=20, choices=YEARS)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    breakfast = models.ForeignKey(Meal, on_delete=models.CASCADE, related_name='breakfast', null=True, blank=True)
    second_breakfast = models.ForeignKey(Meal, on_delete=models.CASCADE, related_name='second_breakfact', null=True, blank=True)
    lunch = models.ForeignKey(Meal, on_delete=models.CASCADE, related_name="lunch", null=True, blank=True)
    tea = models.ForeignKey(Meal, on_delete=models.CASCADE, related_name="tea", null=True, blank=True)
    dinner = models.ForeignKey(Meal, on_delete=models.CASCADE, related_name="dinner", null=True, blank=True)

    def __str__(self):
        return f"{self.date} {self.month} {self.year}"
