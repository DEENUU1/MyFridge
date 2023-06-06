from django.urls import path
from . import views

app_name = "fak"


urlpatterns = [
    path("", views.FakListView.as_view(), name="fak_home"),
    path("fak/<int:pk>/", views.FakDetailsView.as_view(), name="fak_detail"),
    path("fak/create/", views.FakCreateView.as_view(), name="fak_create"),
    path("fak/update/<int:pk>/", views.FakUpdateView.as_view(), name="fak_update"),
    path("fak/delete/<int:pk>/", views.FakDeleteView.as_view(), name="fak_delete"),
    path("medicine/create", views.MedicineCreateView.as_view(), name="medicine_create"),
    path(
        "medicine/update/<int:pk>/",
        views.MedicineUpdateView.as_view(),
        name="medicine_update",
    ),
    path(
        "medicine/delete/<int:pk>/",
        views.MedicineDeleteView.as_view(),
        name="medicine_delete",
    ),
]
