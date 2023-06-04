from django.db.models import Count

from .models import (
    Type,
    Country,
    MainIngredient,
    OtherIngredient,
    DifficultyLevel,
    DishCategory,
    TimeToMake,
    Dish,
)

from django.forms import ModelMultipleChoiceField
from django import forms
from django.db import models


from django import forms
from .models import MainIngredient, Dish


class DishFilterForm(forms.Form):
    # TODO
    # This filter works but still has some bugs
    # For example it returns all dishes with matching ingredients
    # But should return only dishes with at least 60% of ingredients
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        types = Type.objects.all()
        for type in types:
            field_name = f"main_ingredient_{type.id}"
            field_label = f"Main Ingredient ({type.name})"
            self.fields[field_name] = forms.MultipleChoiceField(
                choices=[
                    (str(ingredient.id), str(ingredient))
                    for ingredient in MainIngredient.objects.filter(type=type)
                ],
                label=field_label,
                required=False,
                widget=forms.CheckboxSelectMultiple,
            )

    def filter_dishes(self):
        main_ingredients = []
        for field_name, field_value in self.cleaned_data.items():
            if field_name.startswith("main_ingredient_") and field_value:
                main_ingredients.extend(field_value)

        if main_ingredients:
            total_ingredients = len(main_ingredients)
            dishes = (
                Dish.objects.filter(main_ingredient__in=main_ingredients)
                .annotate(matching_ingredients=Count("main_ingredient"))
                .distinct()
            )
            matching_dishes = []

            for dish in dishes:
                if dish.matching_ingredients >= total_ingredients * 0.6:
                    matching_dishes.append(dish)

            return matching_dishes
        else:
            return Dish.objects.all()


class DateSortingForm(forms.Form):
    CHOICES = (("1", "Newest"), ("2", "Oldest"))

    order_by = forms.ChoiceField(
        choices=CHOICES,
        required=False,
    )


class GlutenFilterForm(forms.Form):
    gluten = forms.BooleanField(required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["gluten"].label = "Has gluten"


class LactoseFilterForm(forms.Form):
    lactose = forms.BooleanField(required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["lactose"].label = "Has lactose"
