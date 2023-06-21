from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from notifications.signals import notify


class CustomUser(AbstractUser):
    description = models.CharField(max_length=200, default=None, blank=True, null=True)
    image = models.ImageField(upload_to="images", default=None, blank=True, null=True)
    newsletter = models.BooleanField(default=False)
    points = models.IntegerField(default=0)
    following = models.ManyToManyField(
        "self", through="UserFollowing", related_name="followed_by", symmetrical=False
    )


class UserFollowing(models.Model):
    user_id = models.ForeignKey(
        CustomUser, related_name="follows", on_delete=models.CASCADE
    )
    following_user_id = models.ForeignKey(
        CustomUser, related_name="followed", on_delete=models.CASCADE
    )
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user_id} is following {self.following_user_id}"


def notification_new_follower(sender, instance, created, **kwargs):
    if created:
        notify.send(
            instance.user_id,
            recipient=instance.following_user_id,
            verb=f"{instance.user_id} is now following you!",
            target=instance,
        )


post_save.connect(notification_new_follower, sender=UserFollowing)
