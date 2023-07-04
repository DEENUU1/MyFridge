from .models import UserDailyStatistics
from users.models import CustomUser
from datetime import datetime, timedelta


def calculate_weight_last_30_days(user_id):
    current_date = datetime.now()
    date_30_days_ago = current_date - timedelta(days=30)

    weight_records = UserDailyStatistics.objects.filter(
        date_created__gte=date_30_days_ago, user_id=user_id
    ).order_by("date_created")

    if weight_records.exists():
        weight_30_days_ago = weight_records.first().weight
        current_weight = weight_records.last().weight

        diff = current_weight - weight_30_days_ago

        return diff

    return None


# TODO calculate weight in current year


# TODO display difference between current and previous day
