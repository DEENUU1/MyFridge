from django.db import models
from users.models import CustomUser


class Type(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        ordering = ("name",)
        verbose_name = "Type"
        verbose_name_plural = "Types"

    def __str__(self):
        return self.name


class Country(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        ordering = ("name",)
        verbose_name = "Country"
        verbose_name_plural = "Countries"

    def __str__(self):
        return self.name


class MainIngredient(models.Model):
    name = models.CharField(max_length=50)
    type = models.ForeignKey(Type, on_delete=models.CASCADE)

    class Meta:
        ordering = ("name",)
        verbose_name = "MainIngredient"
        verbose_name_plural = "MainIngredients"

    def __str__(self):
        return self.name


class OtherIngredient(models.Model):
    name = models.CharField(max_length=50)
    type = models.ForeignKey(Type, on_delete=models.CASCADE)

    class Meta:
        ordering = ("name",)
        verbose_name = "OtherIngredient"
        verbose_name_plural = "OtherIngredients"

    def __str__(self):
        return self.name


class DifficultyLevel(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        ordering = ("name",)
        verbose_name = "DifficultyLevel"
        verbose_name_plural = "DifficultyLevels"

    def __str__(self):
        return self.name


class DishCategory(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        ordering = ("name",)
        verbose_name = "DishCategory"
        verbose_name_plural = "DishCategories"

    def __str__(self):
        return self.name


class TimeToMake(models.Model):
    time = models.IntegerField()
    name = models.CharField(max_length=50)

    class Meta:
        ordering = ("time",)
        verbose_name = "TimeToMake"
        verbose_name_plural = "TimeToMake"

    def __str__(self):
        return f"{self.time} {self.name}"


class Dish(models.Model):
    name = models.CharField(max_length=50)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    time_to_make = models.ForeignKey(TimeToMake, on_delete=models.CASCADE)
    description = models.TextField()
    image = models.ImageField(upload_to="images", default=None, blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_edited = models.DateTimeField(auto_now=True)
    kcal = models.IntegerField(null=True, blank=True)
    gluten = models.BooleanField(default=False)
    lactose = models.BooleanField(default=False)
    meal = models.BooleanField(default=False)  # TODO change meal to meat!
    vegetarian = models.BooleanField(default=False)
    vegan = models.BooleanField(default=False)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    level = models.ForeignKey(DifficultyLevel, on_delete=models.CASCADE)
    main_ingredient = models.ManyToManyField(MainIngredient)
    other_ingredients = models.ManyToManyField(OtherIngredient)
    category = models.ForeignKey(DishCategory, on_delete=models.CASCADE)

    class Meta:
        ordering = ("name",)
        verbose_name = "Dish"
        verbose_name_plural = "Dishes"

    def __str__(self):
        return self.name
