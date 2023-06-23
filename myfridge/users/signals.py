from .models import UserFollowing
from django.db.models.signals import post_save
from notifications.signals import notify
from django.dispatch import receiver
from algorithms.hate_speech import hate_speech_result
from .models import CustomUser


@receiver(post_save, sender=CustomUser)
def handle_new_post(sender, instance, **kwargs):
    counter_text, new_text_text = hate_speech_result(instance.description, "Post")
    if counter_text == 0:
        return

    return CustomUser.objects.filter(id=instance.id).update(description=new_text_text)


post_save.connect(handle_new_post, sender=CustomUser)


def notification_new_follower(sender, instance, created, **kwargs):
    if created:
        notify.send(
            instance.user_id,
            recipient=instance.following_user_id,
            verb=f"{instance.user_id} is now following you!",
            target=instance,
        )


post_save.connect(notification_new_follower, sender=UserFollowing)
