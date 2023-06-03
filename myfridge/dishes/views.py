from typing import Any, Dict

from .models import Dish
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)


class HomeView(ListView):
    model = Dish
    template_name = "home.html"
    paginated_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()

        return queryset

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)

        return context


class DishDetailView(DetailView):
    model = Dish
    template_name = "dish_details.html"

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)

        return context
