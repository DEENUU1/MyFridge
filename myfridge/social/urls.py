from django.urls import path
from . import views

app_name = "social"


urlpatterns = [
    path("dish/<int:pk>/rate-add", views.CreateRateView.as_view(), name="rate-add"),
    path("rate/<int:pk>/update", views.UpdateRateView.as_view(), name="rate-update"),
    path("rate/<int:pk>/delete", views.DeleteRateView.as_view(), name="rate-delete"),
]
