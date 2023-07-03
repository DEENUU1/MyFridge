from typing import Any, Dict

from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils import timezone
from django.views.generic import (
    CreateView,
    DeleteView,
    UpdateView,
    ListView,
    DetailView,
    TemplateView,
)

from .forms import BMIForm, CaloricNeedsForm, PerfectWeightForm
from .models import (
    ShoppingList,
    Meal,
    MealDailyPlan,
    UserDailyStatistics,
)
from django.forms.widgets import DateInput
from django.contrib import messages


def bmiView(request):  # Remove camel case
    if request.method == "POST":
        form = BMIForm(request.POST)
        if form.is_valid():
            bmi = form.calculate_bmi()
            bmi_result = form.return_bmi_result()
            form.save_to_database()
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
            min_weight, max_weight = form.return_perfect_weight()
            form.save_to_database()
            return render(
                request,
                "perfect_weight_result.html",
                {"min_weight": min_weight, "max_weight": max_weight},
            )
    else:
        form = PerfectWeightForm()

    return render(request, "perfect_weight_form.html", {"form": form})


def caloricNeedsView(request):  # Remove camel case
    if request.method == "POST":
        form = CaloricNeedsForm(request.POST)
        if form.is_valid():
            caloric_needs_result = form.return_caloric_needs()
            form.save_to_database()
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

    def get_success_url(self):
        return reverse_lazy("tools:shopping_list")

    def form_valid(self, form):
        form.instance.author = self.request.user
        messages.success(self.request, "Shopping List created successfully.")
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
            messages.error(
                self.request, "You are not authorized to update this Shopping List."
            )
        messages.success(self.request, "Shopping List updated successfully.")
        return queryset


class ShoppingListDeleteView(LoginRequiredMixin, DeleteView):
    model = ShoppingList
    success_url = reverse_lazy("tools:shopping_list")

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(author=self.request.user)
        if not queryset.exists():
            messages.error(
                self.request, "You are not authorized to delete this Shopping List."
            )
        messages.success(self.request, "Shopping List deleted successfully.")
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
        context["bought_items"] = ShoppingList.objects.filter(is_bought=True)
        context["not_bought_items"] = ShoppingList.objects.filter(is_bought=False)
        return context


class MealCreateView(LoginRequiredMixin, CreateView):
    model = Meal
    template_name = "meal_create.html"
    fields = ("name", "content", "url", "dish")

    def get_success_url(self):
        return reverse_lazy("tools:meal_details", kwargs={"pk": self.object.pk})

    def form_valid(self, form):
        form.instance.user = self.request.user
        self.object = form.save()
        messages.success(self.request, "Meal created successfully.")
        return super().form_valid(form)

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        return context


class MealUpdateView(LoginRequiredMixin, UpdateView):
    model = Meal
    template_name = "meal_update.html"
    fields = ("name", "content", "url", "dish")

    def get_success_url(self):
        return reverse_lazy("tools:meal_details", kwargs={"pk": self.kwargs["pk"]})

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(user=self.request.user)
        if not queryset.exists():
            messages.error(self.request, "You are not authorized to update this Meal.")
        messages.success(self.request, "Meal updated successfully.")
        return queryset


class MealDeleteView(LoginRequiredMixin, DeleteView):
    model = Meal
    success_url = reverse_lazy("tools:meal_plan_list")

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(user=self.request.user)
        if not queryset.exists():
            messages.error(self.request, "You are not authorized to delete this Meal.")
        messages.success(self.request, "Meal deleted successfully.")
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
        messages.success(self.request, "Meal Daily Plan created successfully.")
        return super().form_valid(form)

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

    def get_success_url(self):
        return reverse_lazy("tools:meal_plan_details", kwargs={"pk": self.kwargs["pk"]})

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields["date"].widget = DateInput(attrs={"type": "date"})
        return form

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(user=self.request.user)
        if not queryset.exists():
            messages.error(
                self.request, "You are not authorized to update this Meal Daily Plan."
            )
        messages.success(self.request, "Meal Daily Plan updated successfully.")
        return queryset


class MealDailyPlanDeleteView(LoginRequiredMixin, DeleteView):
    model = MealDailyPlan
    success_url = reverse_lazy("tools:meal_plan_list")

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(user=self.request.user)
        if not queryset.exists():
            messages.error(
                self.request, "You are not authorized to delete this Daily Meal Plan."
            )
        messages.success(self.request, "Meal Daily Plan deleted successfully.")
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


class ToolsHomePageTemplateView(TemplateView):
    template_name = "tools_home.html"


# TODO User should be able create only 1 object per day
class UserDailyStatisticsCreateView(LoginRequiredMixin, CreateView):
    model = UserDailyStatistics
    template_name = "user_daily_statistics_create.html"
    success_url = reverse_lazy("dishes:home")
    fields = ("weight",)

    def form_valid(self, form):
        current_date = timezone.now().date()
        user = self.request.user

        if UserDailyStatistics.objects.filter(
            user=user, date_created=current_date
        ).exists():
            messages.error(
                self.request, "You can only add one UserDailyStatistics object per day."
            )
            return self.get_success_url()

        form.instance.user = user
        form.instance.date_created = current_date
        messages.success(self.request, "User Daily Statistics created successfully.")
        return super().form_valid(form)

    def get_success_url(self):
        return self.success_url


class UserDailyStatisticsUpdateView(UpdateView):
    model = UserDailyStatistics
    template_name = "user_daily_statistics_update.html"
    success_url = reverse_lazy("dishes:home")
    fields = ("weight",)

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(user=self.request.user)
        if not queryset.exists():
            messages.error(self.request, "You are not authorized")
        messages.success(self.request, "User Daily Statistics updated successfully.")
        return queryset


class UserDailyStatisticsReportView:
    pass
