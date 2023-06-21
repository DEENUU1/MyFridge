from typing import Any, Dict

from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    UpdateView,
    ListView,
    DetailView,
)

from .forms import BMIForm, CaloricNeedsForm, PerfectWeightForm
from .models import ShoppingList, Meal, MealDailyPlan
from django.forms.widgets import DateInput


def bmiView(request):  # Remove camel case
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


def perfect_weight_view(request):
    if request.method == "POST":
        form = PerfectWeightForm(request.POST)
        if form.is_valid():
            perfect_weight_result = form.return_perfect_weight()
            return render(
                request,
                "perfect_weight_result.html",
                {"perfect_weight_result": perfect_weight_result},
            )
    else:
        form = PerfectWeightForm()

    return render(request, "perfect_weight_form.html", {"form": form})


def caloricNeedsView(request):  # Remove camel case
    if request.method == "POST":
        form = CaloricNeedsForm(request.POST)
        if form.is_valid():
            caloric_needs_result = form.return_caloric_needs()
            return render(
                request,
                "caloric_needs_result.html",
                {"caloric_needs_result": caloric_needs_result},
            )
    else:
        form = CaloricNeedsForm()

    return render(request, "caloric_needs_form.html", {"form": form})


class ShoppingListCreateView(LoginRequiredMixin, CreateView):
    model = ShoppingList
    template_name = "shopping_list_create.html"
    fields = ("name", "quantity")
    success_url = reverse_lazy("tools:shopping_list")
    # TODO success url to created shopping list

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
        # TODO display message after success creation

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)

        return context


class ShoppingListUpdateView(LoginRequiredMixin, UpdateView):
    model = ShoppingList
    template_name = "shopping_list_update.html"
    fields = ("name", "quantity", "is_bought")
    success_url = reverse_lazy("tools:shopping_list")
    # TODO success url to updated shopping list

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(author=self.request.user)
        if not queryset.exists():
            raise PermissionDenied("You are not authorized to edit this Shopping List.")
        # TODO display as a message
        # TODO display message after success update
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
        # TODO display as a message
        # TODO display a message after success delete
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


class MealCreateView(LoginRequiredMixin, CreateView):
    model = Meal
    template_name = "meal_create.html"
    fields = ("name", "content", "url", "dish")
    success_url = reverse_lazy("tools:meal_plan_list")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
        # TODO display a message after success creation

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)

        return context


class MealUpdateView(LoginRequiredMixin, UpdateView):
    model = Meal
    template_name = "meal_update.html"
    fields = ("name", "content", "url", "dish")
    success_url = reverse_lazy("tools:meal_plan_list")

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(user=self.request.user)
        if not queryset.exists():
            raise PermissionDenied("You are not authorized to edit this Meal.")
        # TODO display as a message
        # TODO display message after success update
        return queryset


class MealDeleteView(LoginRequiredMixin, DeleteView):
    model = Meal
    success_url = reverse_lazy("tools:meal_plan_list")

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(user=self.request.user)
        if not queryset.exists():
            raise PermissionDenied("You are not authorized to delete this Meal.")
        # TODO display as a message
        # TODO display a message after success delete
        return queryset


class MealDetailView(LoginRequiredMixin, DetailView):
    model = Meal
    template_name = "meal_detail.html"


class MealDailyPlanCreateView(LoginRequiredMixin, CreateView):
    model = MealDailyPlan
    template_name = "meal_daily_plan_create.html"
    fields = (
        "date",
        "month",
        "year",
        "breakfast",
        "second_breakfast",
        "lunch",
        "tea",
        "dinner",
        "is_public",
    )
    success_url = reverse_lazy("tools:meal_plan_list")

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields["date"].widget = DateInput(attrs={"type": "date"})
        return form

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
        # TODO display a message after success creation

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)

        return context


class MealDailyPlanUpdateView(LoginRequiredMixin, UpdateView):
    model = MealDailyPlan
    template_name = "meal_daily_plan_update.html"
    fields = (
        "date",
        "month",
        "year",
        "breakfast",
        "second_breakfast",
        "lunch",
        "tea",
        "dinner",
        "is_public",
    )
    success_url = reverse_lazy("tools:meal_plan_list")
    # TODO success url to updated meal daily plan

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields["date"].widget = DateInput(attrs={"type": "date"})
        return form

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(user=self.request.user)
        if not queryset.exists():
            raise PermissionDenied(
                "You are not authorized to edit this Meal Daily Plan."
            )
        # TODO display as a message
        # TODO display message after success update
        return queryset


class MealDailyPlanDeleteView(LoginRequiredMixin, DeleteView):
    model = MealDailyPlan
    success_url = reverse_lazy("tools:meal_plan_list")

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(user=self.request.user)
        if not queryset.exists():
            raise PermissionDenied(
                "You are not authorized to delete this Meal Daily Plan."
            )
        # TODO display as a message
        # TODO display a message after success delete
        return queryset


class MealDailyPlanListView(LoginRequiredMixin, ListView):
    model = MealDailyPlan
    template_name = "meal_daily_plan.html"
    paginate_by = 7

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(user=self.request.user)

        return queryset

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        return context


class MealDailyPlanDetailView(LoginRequiredMixin, DetailView):
    model = MealDailyPlan
    template_name = "meal_daily_plan_detail.html"
