from django.db.models.signals import post_save
from notifications.signals import notify
from .models import FavouriteDish, Rate


def notification_dish_add_to_favourite(sender, instance, created, **kwargs):
    if created:
        notify.send(
            instance.user,
            recipient=instance.dish.author,
            verb=f"{instance.user.username} added {instance.dish.name} to favourite",
            target=instance.dish,
        )


post_save.connect(notification_dish_add_to_favourite, sender=FavouriteDish)


def notification_dish_add_rate(sender, instance, created, **kwargs):
    if created:
        notify.send(
            instance.author,
            recipient=instance.dish.author,
            verb=f"{instance.author.username} added rate {instance.choose_rate} to {instance.dish.name}",
            target=instance.dish,
        )


post_save.connect(notification_dish_add_rate, sender=Rate)
