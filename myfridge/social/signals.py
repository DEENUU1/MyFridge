from django.db.models.signals import post_save
from notifications.signals import notify
from .models import FavouriteDish, Rate
from django.db.models.signals import post_save
from .models import Rate
from django.dispatch import receiver
from algorithms.hate_speech import hate_speech_result


@receiver(post_save, sender=Rate)
def handle_new_post(sender, instance, **kwargs):
    counter_text, new_text_text = hate_speech_result(instance.comment, "Rate")
    if counter_text == 0:
        return

    return Rate.objects.filter(id=instance.id).update(comment=new_text_text)


post_save.connect(handle_new_post, sender=Rate)


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
