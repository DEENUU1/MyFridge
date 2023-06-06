from django.apps import AppConfig


class FakConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "fak"
