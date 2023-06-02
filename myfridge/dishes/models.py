from django.db import models
from users.models import CustomUser


class Type(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Country(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class MainIngredient(models.Model):
    name = models.CharField(max_length=50)
    type = models.ForeignKey(Type, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class OtherIngredient(models.Model):
    name = models.CharField(max_length=50)
    type = models.ForeignKey(Type, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class DifficultyLevel(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class DishCategory(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class TimeToMake(models.Model):
    time = models.IntegerField()
    name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.time} {self.name}"


class Dish(models.Model):
    name = models.CharField(max_length=50)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    time_to_make = models.ForeignKey(TimeToMake, on_delete=models.CASCADE)
    description = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_edited = models.DateTimeField(auto_now=True)
    kcal = models.IntegerField(null=True, blank=True)
    gluten = models.BooleanField(default=False)
    lactose = models.BooleanField(default=False)
    meal = models.BooleanField(default=False)
    vegetarian = models.BooleanField(default=False)
    vegan = models.BooleanField(default=False)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    level = models.ForeignKey(DifficultyLevel, on_delete=models.CASCADE)
    main_ingredient = models.ManyToManyField(MainIngredient)
    other_ingredients = models.ManyToManyField(OtherIngredient)
    category = models.ForeignKey(DishCategory, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Rate(models.Model):
    RATES = [(1, "1"), (2, "2"), (3, "3"), (4, "4"), (5, "5")]

    choose_rate = models.IntegerField(choices=RATES)
    date_created = models.DateTimeField(auto_now_add=True)
    comment = models.CharField(max_length=150)
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE, related_name="rates")
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.dish.name} {self.choose_rate}"
