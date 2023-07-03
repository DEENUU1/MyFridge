from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import UserDailyStatistics


@receiver(post_save, sender=UserDailyStatistics)
def update_user_weight(sender, instance, created, **kwargs):
    if created:
        instance.user.current_weight = instance.weight
        instance.user.save()


post_save.connect(update_user_weight, sender=UserDailyStatistics)
