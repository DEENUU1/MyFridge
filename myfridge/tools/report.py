from .models import UserDailyStatistics
from datetime import datetime, timedelta


def calculate_weight_last_30_days(user_id: int) -> int:
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

    return 0


def calculate_weight_last_day(user_id: int) -> int:
    current_date = datetime.now()
    date_1_day_ago = current_date - timedelta(days=1)

    weight_records = UserDailyStatistics.objects.filter(
        date_created__gte=date_1_day_ago, user_id=user_id
    ).order_by("date_created")

    if weight_records.exists():
        return weight_records.last().weight

    return 0
