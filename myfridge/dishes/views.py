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
from social.models import Rate
from .forms import (
    DishFilterForm,
    DateSortingForm,
    GlutenFilterForm,
    LactoseFilterForm,
    MeatFilterForm,
    VeganFilterForm,
    VegetarianFilterForm,
    CountryFilterForm,
)


class HomeView(ListView):
    model = Dish
    template_name = "home.html"
    paginated_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()

        form = DishFilterForm(self.request.GET)
        if form.is_valid():
            queryset = form.filter_dishes()

        order_by = self.request.GET.get("order_by")
        if order_by:
            if order_by == "1":
                queryset = queryset.order_by("date_created")
            if order_by == "2":
                queryset = queryset.order_by("-date_created")

        gluten = self.request.GET.get("gluten")
        if gluten:
            queryset = queryset.filter(gluten=True)

        lactose = self.request.GET.get("lactose")
        if lactose:
            queryset = queryset.filter(lactose=True)

        meat = self.request.GET.get("meat")
        if meat:
            queryset = queryset.filter(meal=True)

        vegan = self.request.GET.get("vegan")
        if vegan:
            queryset = queryset.filter(vegan=True)

        vegetarian = self.request.GET.get("vegetarian")
        if vegetarian:
            queryset = queryset.filter(vegetarian=True)

        country = self.request.GET.get("country")
        if country:
            queryset = queryset.filter(country=country)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["filter_form"] = DishFilterForm(self.request.GET)
        context["date_sorting_form"] = DateSortingForm(self.request.GET)
        context["gluten_form"] = GlutenFilterForm(self.request.GET)
        context["lactose_form"] = LactoseFilterForm(self.request.GET)
        context["meat_form"] = MeatFilterForm(self.request.GET)
        context["vegan_form"] = VeganFilterForm(self.request.GET)
        context["vegetarian_form"] = VegetarianFilterForm(self.request.GET)
        context["country_form"] = CountryFilterForm(self.request.GET)
        return context


class DishDetailView(DetailView):
    model = Dish
    template_name = "dish_details.html"

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["rates"] = Rate.objects.filter(dish=self.object)
        return context


class DishCreateView(CreateView):
    model = Dish
    template_name = "dish_create.html"
    success_url = reverse_lazy("dishes:home")
    fields = (
        "name",
        "time_to_make",
        "description",
        "image",
        "kcal",
        "gluten",
        "lactose",
        "meal",
        "vegetarian",
        "vegan",
        "country",
        "level",
        "main_ingredient",
        "other_ingredients",
        "category",
    )

    def form_valid(self, form):
        form.instance.author = self.request.user

        user = self.request.user
        user.points += 10
        user.save()

        return super().form_valid(form)

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)

        return context


class UpdateDishView(UpdateView):
    model = Dish
    template_name = "dish_update.html"
    success_url = reverse_lazy("dishes:home")
    fields = (
        "name",
        "time_to_make",
        "description",
        "image",
        "kcal",
        "gluten",
        "lactose",
        "meal",
        "vegetarian",
        "vegan",
        "country",
        "level",
        "main_ingredient",
        "other_ingredients",
        "category",
    )

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(author=self.request.user)
        return queryset

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)

        return context


class DeleteDishView(DeleteView):
    model = Dish
    success_url = reverse_lazy("dishes:home")

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(author=self.request.user)
        return queryset
