from django.db.models.signals import post_save
from notifications.signals import notify
from .models import Comment, Post
from django.dispatch import receiver
from algorithms.hate_speech import hate_speech_result


def notification_post_add_comment(sender, instance, created, **kwargs):
    if created:
        notify.send(
            instance.author,
            recipient=instance.post.author,
            verb=f"{instance.author.username} commented on your post {instance.post.title}",
            target=instance.post,
        )


post_save.connect(notification_post_add_comment, sender=Comment)


@receiver(post_save, sender=Comment)
def handle_new_comment(sender, instance, **kwargs):
    counter, new_text = hate_speech_result(instance.text, "Comment")
    if counter == 0:
        return
    # elif 0 < counter < 2:
    return Comment.objects.filter(id=instance.id).update(text=new_text)
    # Comment.objects.filter(id=instance.id).delete().delete()


post_save.connect(handle_new_comment, sender=Comment)


@receiver(post_save, sender=Post)
def handle_new_post(sender, instance, **kwargs):
    counter_text, new_text_text = hate_speech_result(instance.text, "Post")
    if counter_text == 0:
        return

    # elif 0 < counter < 2:
    return Post.objects.filter(id=instance.id).update(text=new_text_text)
    # Post.objects.filter(id=instance.id).delete().delete()


post_save.connect(handle_new_post, sender=Post)
