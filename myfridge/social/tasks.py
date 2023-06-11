import random

from celery import shared_task
from users.models import CustomUser
from dishes.models import Dish
from django.core.mail import send_mail
from users.task import send_email_task


def get_users_with_newsletter_true():
    return CustomUser.objects.filter(newsletter=True)


def get_random_dish():
    dishes = Dish.objects.all()
    random_dish = random.choice(dishes)
    return random_dish

