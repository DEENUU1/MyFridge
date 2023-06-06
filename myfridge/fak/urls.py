from django.urls import path
from . import views

app_name = "fak"


urlpatterns = [
    path("", views.FakListView.as_view(), name="fak_home"),
    path("create/", views.FakCreateView.as_view(), name="fak_create"),
    path("update/<int:pk>/", views.FakUpdateView.as_view(), name="fak_update"),
]
