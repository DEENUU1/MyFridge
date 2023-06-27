from celery import shared_task
from .fake_data import (
    create_fake_user_data,
    create_fake_shopping_list,
    create_fake_meal,
    create_fake_daily_meal_plan,
    create_fake_caloric_needs,
    create_fake_perfect_weight,
    create_fake_bmi,
)


@shared_task()
def task_create_fake_user_data():
    create_fake_user_data()


@shared_task()
def task_create_fake_shopping_list():
    create_fake_shopping_list()


@shared_task()
def task_create_fake_meal():
    create_fake_meal()


@shared_task()
def task_create_daily_meal_plan():
    create_fake_daily_meal_plan()


@shared_task()
def task_create_fake_caloric_needs():
    create_fake_caloric_needs()


@shared_task()
def task_create_fake_perfect_weight():
    create_fake_perfect_weight()


@shared_task()
def task_create_fake_bmi():
    create_fake_bmi()
