from celery import shared_task
from .models import Medicine
import datetime
from users.task import send_email_task


@shared_task()
def send_medicine_expired_notification():
    expired_medicines = Medicine.objects.filter(expiration_date__lt=datetime.datetime.now())
    SUBJECT = "Your medicine is expired"
    MESSAGE = f"Your medicine {expired_medicines.name} is expired"

    for medicine in expired_medicines:
        send_email_task(
            [medicine.user.email],
            SUBJECT,
            MESSAGE,
        )


