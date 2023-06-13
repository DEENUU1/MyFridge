from typing import Any, Dict

from django.shortcuts import render
from django.urls import reverse_lazy

from .models import Fak, Medicine
from django.core.exceptions import PermissionDenied
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
    DetailView,
    FormView
)

from django.contrib.auth.mixins import LoginRequiredMixin


class FakListView(ListView):
    model = Fak
    template_name = "fak_list.html"
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(author=self.request.user)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class FakCreateView(LoginRequiredMixin, CreateView):
    model = Fak
    template_name = "fak_create.html"
    fields = ("name",)
    success_url = reverse_lazy("fak:fak_home")

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)

        return context


class FakUpdateView(LoginRequiredMixin, UpdateView):
    model = Fak
    template_name = "fak_update.html"
    fields = ("name",)
    success_url = reverse_lazy("fak:fak_home")

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(author=self.request.user)
        if not queryset.exists():
            raise PermissionDenied("You are not authorized to edit this Fak.")
        return queryset


class FakDeleteView(LoginRequiredMixin, DeleteView):
    model = Fak
    success_url = reverse_lazy("fak:fak_home")

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(author=self.request.user)
        if not queryset.exists():
            raise PermissionDenied("You are not authorized to edit this Fak.")
        return queryset


class MedicineCreateView(LoginRequiredMixin, CreateView):
    model = Medicine
    template_name = "medicine_create.html"
    fields = ("name", "expiration_date", "quantity", "fak")
    success_url = reverse_lazy("fak:fak_home")

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)

        return context


class MedicineUpdateView(LoginRequiredMixin, UpdateView):
    model = Medicine
    template_name = "medicine_update.html"
    fields = ("name", "expiration_date", "quantity", "fak")
    success_url = reverse_lazy("fak:fak_home")

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(author=self.request.user)
        if not queryset.exists():
            raise PermissionDenied("You are not authorized to edit this Medicine.")
        return queryset


class MedicineDeleteView(LoginRequiredMixin, DeleteView):
    model = Medicine
    success_url = reverse_lazy("fak:fak_home")

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(author=self.request.user)
        if not queryset.exists():
            raise PermissionDenied("You are not authorized to delete this Medicine.")
        return queryset


class FakDetailsView(LoginRequiredMixin, DetailView):
    model = Fak
    template_name = "fak_details.html"
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(author=self.request.user)

        return queryset

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["medicines"] = Medicine.objects.filter(fak=self.object)
        return context
