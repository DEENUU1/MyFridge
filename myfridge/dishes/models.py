from django.db import models


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
    #author = ...
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
    #rates = ...
    level = models.ForeignKey(DifficultyLevel, on_delete=models.CASCADE)
    main_ingredient = models.ManyToManyField(MainIngredient)
    other_ingredients = models.ManyToManyField(OtherIngredient)
    category = models.ForeignKey(DishCategory, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

