from celery import shared_task
from django.conf import settings
from django.core.mail import send_mail
from django.core.files.base import ContentFile
from .models import CustomUser
import requests


@shared_task()
def send_email_task(email, subject, message):
    send_mail(subject, message, settings.EMAIL_HOST_USER, [email])


@shared_task()
def add_profile_picture(user_id, image_url):
    user = CustomUser.objects.get(user_id=user_id)
    response = requests.get(image_url)
    image_name = image_url.split("/")[-1]
    user.image.save(image_name, ContentFile(response.content), save=True)