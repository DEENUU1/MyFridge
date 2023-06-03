from django.shortcuts import render, get_object_or_404
from .models import Rate
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)

from dishes.models import Dish


class CreateRateView(CreateView):
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
