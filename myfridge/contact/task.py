from datetime import timedelta
from celery import shared_task
from django.utils import timezone
from .models import Contact


@shared_task
def delete_old_contacts():
    time_threshold = timezone.now() - timedelta(days=60)
    Contact.objects.filter(date_created__lte=time_threshold).delete()
