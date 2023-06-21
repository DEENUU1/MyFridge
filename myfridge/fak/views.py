from typing import Any, Dict

from django.urls import reverse_lazy

from .models import Fak, Medicine
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
    DetailView,
)
from django.forms.widgets import DateInput
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages


class FakListView(LoginRequiredMixin, ListView):
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

    def get_success_url(self):
        return reverse_lazy("fak:fak_detail", kwargs={"pk": self.object.pk})

    def form_valid(self, form):
        form.instance.author = self.request.user
        messages.success(self.request, "Fak created successfully")
        return super().form_valid(form)

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        return context


class FakUpdateView(LoginRequiredMixin, UpdateView):
    model = Fak
    template_name = "fak_update.html"
    fields = ("name",)

    def get_success_url(self):
        return reverse_lazy("fak:fak_detail", kwargs={"pk": self.object.pk})

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(author=self.request.user)
        if not queryset.exists():
            messages.error(self.request, "You are not authorized to edit this Fak.")
        messages.success(self.request, "Fak updated successfully")
        return queryset


class FakDeleteView(LoginRequiredMixin, DeleteView):
    model = Fak
    success_url = reverse_lazy("fak:fak_home")

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(author=self.request.user)
        if not queryset.exists():
            messages.error(self.request, "You are not authorized to delete this Fak.")
        messages.success(self.request, "Fak deleted successfully")
        return queryset


class MedicineCreateView(LoginRequiredMixin, CreateView):
    model = Medicine
    template_name = "medicine_create.html"
    fields = ("name", "expiration_date", "quantity", "fak")

    def get_success_url(self):
        return reverse_lazy("fak:fak_detail", kwargs={"pk": self.object.fak.pk})

    def form_valid(self, form):
        form.instance.author = self.request.user
        messages.success(self.request, "Medicine created successfully")
        return super().form_valid(form)

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields["expiration_date"].widget = DateInput(attrs={"type": "date"})
        return form

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        return context


class MedicineUpdateView(LoginRequiredMixin, UpdateView):
    model = Medicine
    template_name = "medicine_update.html"
    fields = ("name", "expiration_date", "quantity", "fak")

    def get_success_url(self):
        return reverse_lazy("fak:fak_detail", kwargs={"pk": self.object.fak.pk})

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(author=self.request.user)
        if not queryset.exists():
            messages.error(
                self.request, "You are not authorized to edit this Medicine."
            )
        messages.success(self.request, "Medicine updated successfully")
        return queryset


class MedicineDeleteView(LoginRequiredMixin, DeleteView):
    model = Medicine

    def get_success_url(self):
        return reverse_lazy("fak:fak_detail", kwargs={"pk": self.object.fak.pk})

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(author=self.request.user)
        if not queryset.exists():
            messages.error(
                self.request, "You are not authorized to delete this Medicine."
            )
        messages.success(self.request, "Medicine deleted successfully")
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
