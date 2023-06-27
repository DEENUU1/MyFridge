from celery import shared_task
from .fake_data import create_fake_user_data


@shared_task()
def task_create_fake_user_data():
    create_fake_user_data()
