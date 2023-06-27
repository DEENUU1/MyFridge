from django.core.management.base import BaseCommand
from algorithms.tasks import (
    task_create_fake_user_data,
    task_create_fake_shopping_list,
    task_create_fake_meal,
    task_create_daily_meal_plan,
    task_create_fake_caloric_needs,
    task_create_fake_perfect_weight,
    task_create_fake_bmi,
    task_create_fake_feedback,
    task_create_fake_fak,
    task_create_fake_medicine,
    task_create_fake_type,
    task_create_fake_country,
    task_create_fake_main_ingredient,
    task_create_fake_other_ingredient,
    task_create_difficulty_level,
    task_create_dish_category,
    task_create_fake_time_to_make,
    task_create_fake_dish,
    task_create_fake_rate,
    task_create_fake_favourite_dish,
    task_create_fake_post,
    task_create_fake_comment,
)


class Command(BaseCommand):
    help = "Load fake data into models"

    def handle(self, *args, **options):
        task_create_fake_user_data.delay()
        task_create_fake_shopping_list.delay()
        task_create_fake_meal.delay()
        task_create_daily_meal_plan.delay()
        task_create_fake_caloric_needs.delay()
        task_create_fake_perfect_weight.delay()
        task_create_fake_bmi.delay()
        task_create_fake_feedback.delay()
        task_create_fake_fak.delay()
        task_create_fake_medicine.delay()
        task_create_fake_type.delay()
        task_create_fake_country.delay()
        task_create_fake_main_ingredient.delay()
        task_create_fake_other_ingredient.delay()
        task_create_difficulty_level.delay()
        task_create_dish_category.delay()
        task_create_fake_time_to_make.delay()
        task_create_fake_dish.delay()
        task_create_fake_rate.delay()
        task_create_fake_favourite_dish.delay()
        task_create_fake_post.delay()
        task_create_fake_comment.delay()
