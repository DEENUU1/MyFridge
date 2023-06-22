from django.db.models.signals import post_save
from notifications.signals import notify
from .models import Comment


def notification_post_add_comment(sender, instance, created, **kwargs):
    if created:
        notify.send(
            instance.author,
            recipient=instance.post.author,
            verb=f"{instance.author.username} commented on your post {instance.post.title}",
            target=instance.post,
        )


post_save.connect(notification_post_add_comment, sender=Comment)
