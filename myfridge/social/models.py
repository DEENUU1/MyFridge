from django.db import models
from dishes.models import Dish
from users.models import CustomUser


class Rate(models.Model):
    RATES = [(1, "1"), (2, "2"), (3, "3"), (4, "4"), (5, "5")]

    choose_rate = models.IntegerField(choices=RATES)
    date_created = models.DateTimeField(auto_now_add=True)
    comment = models.CharField(max_length=150)
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE, related_name="rates")
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    class Meta:
        ordering = ("choose_rate",)
        verbose_name = "Rate"
        verbose_name_plural = "Rates"

    def __str__(self):
        return f"{self.dish.name} {self.choose_rate}"