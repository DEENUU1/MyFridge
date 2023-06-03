from django.urls import path
from . import views

app_name = "social"


urlpatterns = [
    path("dish/<int:pk>/rate-add", views.CreateRateView.as_view(), name="rate-add"),
]
