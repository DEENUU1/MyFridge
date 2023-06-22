from django.db.models.signals import post_save
from notifications.signals import notify
from .models import UserFollowing


def notification_new_follower(sender, instance, created, **kwargs):
    if created:
        notify.send(
            instance.user_id,
            recipient=instance.following_user_id,
            verb=f"{instance.user_id} is now following you!",
            target=instance,
        )


post_save.connect(notification_new_follower, sender=UserFollowing)
