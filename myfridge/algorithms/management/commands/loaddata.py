from django.core.management.base import BaseCommand
from algorithms.tasks import (
    task_create_fake_user_data,
    task_create_fake_shopping_list,
    task_create_fake_meal,
    task_create_daily_meal_plan,
    task_create_fake_caloric_needs,
    task_create_fake_perfect_weight,
    task_create_fake_bmi,
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
