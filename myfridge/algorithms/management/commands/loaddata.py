from django.core.management.base import BaseCommand
from algorithms.tasks import task_create_fake_user_data


class Command(BaseCommand):
    help = "Load fake data into models"

    def handle(self, *args, **options):
        task_create_fake_user_data.delay()
