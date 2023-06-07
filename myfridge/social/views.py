from django.core.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404, redirect
from django.views import View

from .models import Rate, FavouriteDish
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)

from dishes.models import Dish
from users.models import CustomUser
from typing import Dict, Any
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import F


class CreateRateView(LoginRequiredMixin, CreateView):
    model = Rate
    fields = ("choose_rate", "comment")
    success_url = reverse_lazy("dishes:home")
    template_name = "rate_create.html"

    def form_valid(self, form):
        form.instance.author = self.request.user
        dish = get_object_or_404(Dish, pk=self.kwargs["pk"])
        form.instance.dish = dish

        user = self.request.user
        user.points += 1
        user.save()

        if form.instance.choose_rate >= 4:
            author = dish.author
            author.points += 1
            author.save()

        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["dish"] = self.kwargs["pk"]
        return context


class UpdateRateView(LoginRequiredMixin, UpdateView):
    model = Rate
    fields = ("choose_rate", "comment")
    template_name = "rate_update.html"
    success_url = reverse_lazy("dishes:home")

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(author=self.request.user)
        if not queryset.exists():
            raise PermissionDenied("You are not authorized to edit this Rate.")
        return queryset

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["dish"] = self.kwargs["pk"]
        return context


class DeleteRateView(LoginRequiredMixin, DeleteView):
    model = Rate
    success_url = reverse_lazy("dishes:home")

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(author=self.request.user)
        if not queryset.exists():
            raise PermissionDenied("You are not authorized to delete this Rate.")
        return queryset

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["dish"] = self.kwargs["pk"]
        return context


class UserRankingView(ListView):
    model = CustomUser
    template_name = "user_ranking.html"
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.order_by("-points")
        return queryset

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        return context


class AddToFavouritesView(LoginRequiredMixin, View):
    def post(self, request, dish_id):
        dish = get_object_or_404(Dish, pk=dish_id)
        user = request.user
        existing_favourite = FavouriteDish.objects.filter(user=user, dish=dish)
        if existing_favourite:
            return redirect("dishes:home")

        favourite_dish = FavouriteDish(user=user, dish=dish)
        favourite_dish.save()

        dish.author.points = F("points") + 3
        dish.author.save()

        return redirect("dishes:home")
