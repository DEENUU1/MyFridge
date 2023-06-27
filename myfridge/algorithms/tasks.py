from celery import shared_task
from .fake_data import (
    create_fake_user_data,
    create_fake_shopping_list,
    create_fake_meal,
    create_fake_daily_meal_plan,
    create_fake_caloric_needs,
    create_fake_perfect_weight,
    create_fake_bmi,
    create_fake_feedback,
    create_fake_fak,
    create_fake_medicine,
    create_fake_type,
    create_fake_country,
    create_fake_main_ingredient,
    create_fake_other_ingredient,
    create_difficulty_leveL,
    create_dish_category,
    create_fake_time_to_make,
    create_fake_dish,
    create_fake_rate,
    create_fake_favourite_dish,
    create_fake_post,
    create_fake_comment,
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


@shared_task()
def task_create_fake_feedback():
    create_fake_feedback()


@shared_task()
def task_create_fake_fak():
    create_fake_fak()


@shared_task()
def task_create_fake_medicine():
    create_fake_medicine()


@shared_task()
def task_create_fake_type():
    create_fake_type()


@shared_task()
def task_create_fake_country():
    create_fake_country()


@shared_task()
def task_create_fake_main_ingredient():
    create_fake_main_ingredient()


@shared_task()
def task_create_fake_other_ingredient():
    create_fake_other_ingredient()


@shared_task()
def task_create_difficulty_level():
    create_difficulty_leveL()


@shared_task()
def task_create_dish_category():
    create_dish_category()


@shared_task()
def task_create_fake_time_to_make():
    create_fake_time_to_make()


@shared_task()
def task_create_fake_dish():
    create_fake_dish()


@shared_task()
def task_create_fake_rate():
    create_fake_rate()


@shared_task()
def task_create_fake_favourite_dish():
    create_fake_favourite_dish()


@shared_task()
def task_create_fake_post():
    create_fake_post()


@shared_task()
def task_create_fake_comment():
    create_fake_comment()
