from typing import Any, Dict

from django.core.exceptions import PermissionDenied
from django.db.models import Q

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
    DateSortingForm,
    GlutenFilterForm,
    LactoseFilterForm,
    MeatFilterForm,
    VeganFilterForm,
    VegetarianFilterForm,
    CountryFilterForm,
    DifficultyLevelFilterForm,
    CategoryFilterForm,
    CaloriesSortingForm,
    SearchForm,
    MainIngredientForm,
)
from django.contrib.auth.mixins import LoginRequiredMixin


class HomeView(ListView):
    model = Dish
    template_name = "home.html"
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()

        main_ingredients = self.request.GET.get("ingredients")
        if main_ingredients:
            queryset = queryset.filter(main_ingredient__in=main_ingredients)

        search_query = self.request.GET.get("search_query")
        if search_query:
            ingredients = [ingredient.strip() for ingredient in search_query.split(",")]
            conditions = [Q(main_ingredient__name__icontains=ingredient) for ingredient in ingredients]
            combined_conditions = conditions[0]
            for condition in conditions[1:]:
                combined_conditions |= condition
            queryset = queryset.filter(combined_conditions).distinct()

        order_by = self.request.GET.get("order_by")
        if order_by:
            if order_by == "1":
                queryset = queryset.order_by("date_created")
            if order_by == "2":
                queryset = queryset.order_by("-date_created")

        calories = self.request.GET.get("calories")
        if calories:
            if calories == "1":
                queryset = queryset.order_by("calories")
            if calories == "2":
                queryset = queryset.order_by("-calories")

        time_to_make = self.request.GET.get("time_to_make")
        if time_to_make:
            if time_to_make == "1":
                queryset = queryset.order_by("time_to_make")
            if time_to_make == "2":
                queryset = queryset.order_by("-time_to_make")

        gluten = self.request.GET.get("gluten")
        if gluten:
            queryset = queryset.filter(gluten=True)

        lactose = self.request.GET.get("lactose")
        if lactose:
            queryset = queryset.filter(lactose=True)

        meat = self.request.GET.get("meat")
        if meat:
            queryset = queryset.filter(meat=True)

        vegan = self.request.GET.get("vegan")
        if vegan:
            queryset = queryset.filter(vegan=True)

        vegetarian = self.request.GET.get("vegetarian")
        if vegetarian:
            queryset = queryset.filter(vegetarian=True)

        country = self.request.GET.get("country")
        if country:
            queryset = queryset.filter(country=country)

        level = self.request.GET.get("level")
        if level:
            queryset = queryset.filter(level=level)

        category = self.request.GET.get("category")
        if category:
            queryset = queryset.filter(category=category)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["date_sorting_form"] = DateSortingForm(self.request.GET)
        context["gluten_form"] = GlutenFilterForm(self.request.GET)
        context["lactose_form"] = LactoseFilterForm(self.request.GET)
        context["meat_form"] = MeatFilterForm(self.request.GET)
        context["vegan_form"] = VeganFilterForm(self.request.GET)
        context["vegetarian_form"] = VegetarianFilterForm(self.request.GET)
        context["country_form"] = CountryFilterForm(self.request.GET)
        context["difficulty_level_form"] = DifficultyLevelFilterForm(self.request.GET)
        context["category_form"] = CategoryFilterForm(self.request.GET)
        context["calories_sorting_form"] = CaloriesSortingForm(self.request.GET)
        context["search_form"] = SearchForm(self.request.GET)
        context["main_ingredient_form"] = MainIngredientForm(self.request.GET)
        search_query = self.request.GET.get("search_query")
        context["search_query"] = search_query if search_query else None
        return context


class DishDetailView(DetailView):
    model = Dish
    template_name = "dish_details.html"

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["rates"] = Rate.objects.filter(dish=self.object)
        return context


class DishCreateView(LoginRequiredMixin, CreateView):
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
        "meat",
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


class UpdateDishView(LoginRequiredMixin, UpdateView):
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
        "meat",
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
        if not queryset.exists():
            raise PermissionDenied("You are not authorized to edit this Dish.")
        return queryset

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)

        return context


class DeleteDishView(LoginRequiredMixin, DeleteView):
    model = Dish

    success_url = reverse_lazy("dishes:home")

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(author=self.request.user)
        if not queryset.exists():
            raise PermissionDenied("You are not authorized to edit this Dish.")
        return queryset

