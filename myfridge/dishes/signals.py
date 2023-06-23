from django.db.models.signals import post_save
from .models import Dish
from django.dispatch import receiver
from algorithms.hate_speech import hate_speech_result


@receiver(post_save, sender=Dish)
def handle_new_post(sender, instance, **kwargs):
    counter_text, new_text_text = hate_speech_result(instance.description, "Post")
    if counter_text == 0:
        return

    return Dish.objects.filter(id=instance.id).update(description=new_text_text)


post_save.connect(handle_new_post, sender=Dish)
