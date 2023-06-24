from django.db import models
from dishes.models import Dish
from users.models import CustomUser
from django.utils import timezone
from datetime import timedelta


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

    @property
    def get_newest_label(self) -> bool:
        """
        Check if the rate is newer than 12 hours.
        :return: bool
        """
        if self.date_created > timezone.now() - timedelta(hours=12):
            return True
        return False


class Feedback(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    message = models.CharField(max_length=150)

    class Meta:
        ordering = ("date_created",)
        verbose_name = "Feedback"
        verbose_name_plural = "Feedbacks"

    def __str__(self):
        return f"{self.message[:15]}"


class FavouriteDish(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Favourite dish"
        verbose_name_plural = "Favourite dishes"
        unique_together = ("user", "dish")

    def __str__(self):
        return f"{self.user} {self.dish.name}"
