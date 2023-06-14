from django.db import models
from users.models import CustomUser
from ckeditor.fields import RichTextField


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


class Quantity(models.Model):
    value = models.IntegerField()
    unit = models.CharField()

    class Meta:
        ordering = ("value",)
        verbose_name = "Quantity"
        verbose_name_plural = "Quantities"

    def __str__(self):
        return f"{self.value} {self.unit}"


class MainIngredient(models.Model):
    name = models.CharField(max_length=50)
    type = models.ForeignKey(Type, on_delete=models.CASCADE)
    quantity = models.ForeignKey(Quantity, on_delete=models.CASCADE, null=True)

    class Meta:
        ordering = ("name",)
        verbose_name = "MainIngredient"
        verbose_name_plural = "MainIngredients"

    def __str__(self):
        return self.name


class OtherIngredient(models.Model):
    name = models.CharField(max_length=50)
    type = models.ForeignKey(Type, on_delete=models.CASCADE)
    quantity = models.ForeignKey(Quantity, on_delete=models.CASCADE, null=True)

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
    value = models.IntegerField()

    class Meta:
        ordering = ("value",)
        verbose_name = "TimeToMake"
        verbose_name_plural = "TimeToMake"

    def __str__(self):
        return str(self.value)

    @property
    def get_values(self):
        if self.value == 1:
            return "1 minute"
        return f"{self.value} minutes"


class Dish(models.Model):
    name = models.CharField(max_length=50)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    time_to_make = models.ForeignKey(TimeToMake, on_delete=models.CASCADE)
    description = RichTextField(blank=True, null=True)
    image = models.ImageField(upload_to="images", default=None, blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_edited = models.DateTimeField(auto_now=True)
    kcal = models.IntegerField(null=True, blank=True)
    gluten = models.BooleanField(default=False)
    lactose = models.BooleanField(default=False)
    meat = models.BooleanField(default=False)
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
