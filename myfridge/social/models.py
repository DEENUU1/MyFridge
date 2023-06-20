from django.db import models
from dishes.models import Dish
from users.models import CustomUser
from django.db.models.signals import post_save
from notifications.signals import notify


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


def notification_dish_add_to_favourite(sender, instance, created, **kwargs):
    if created:
        notify.send(
            instance.user,
            recipient=instance.dish.author,
            verb=f"{instance.user.username} added {instance.dish.name} to favourite",
            target=instance.dish
            )
post_save.connect(notification_dish_add_to_favourite, sender=FavouriteDish)