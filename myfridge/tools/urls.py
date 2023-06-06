from django.urls import path
from . import views

app_name = "tools"


urlpatterns = [
    path("bmi/", views.bmiView, name="bmi"),
]
