from typing import Any, Dict

from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, UpdateView, ListView

from .forms import BMIForm
from .models import ShoppingList


def bmiView(request):
    if request.method == "POST":
        form = BMIForm(request.POST)
        if form.is_valid():
            bmi = form.calculate_bmi()
            bmi_result = form.return_bmi_result()
            return render(
                request, "bmi_result.html", {"bmi": bmi, "bmi_result": bmi_result}
            )
    else:
        form = BMIForm()

    return render(request, "bmi_form.html", {"form": form})


class ShoppingListCreateView(LoginRequiredMixin, CreateView):
    model = ShoppingList
    template_name = "shopping_list_create.html"
    fields = ("name", "quantity")
    success_url = reverse_lazy("tools:shopping_list")

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)

        return context


class ShoppingListUpdateView(LoginRequiredMixin, UpdateView):
    model = ShoppingList
    template_name = "shopping_list_update.html"
    fields = ("name", "quantity", "is_bought")
    success_url = reverse_lazy("tools:shopping_list")

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(author=self.request.user)
        if not queryset.exists():
            raise PermissionDenied("You are not authorized to edit this Shopping List.")
        return queryset


class ShoppingListDeleteView(LoginRequiredMixin, DeleteView):
    model = ShoppingList
    success_url = reverse_lazy("tools:shopping_list")

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(author=self.request.user)
        if not queryset.exists():
            raise PermissionDenied(
                "You are not authorized to delete this Shopping List."
            )
        return queryset


class ShoppingListView(LoginRequiredMixin, ListView):
    model = ShoppingList
    template_name = "shopping_list.html"
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(author=self.request.user)

        return queryset

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        return context
