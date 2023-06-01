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


