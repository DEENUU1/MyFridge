from django import forms
from .models import (
    Country,
    DifficultyLevel,
    DishCategory,
)


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


class MeatFilterForm(forms.Form):
    meat = forms.BooleanField(required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["meat"].label = "Has meat"


class VeganFilterForm(forms.Form):
    vegan = forms.BooleanField(required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["vegan"].label = "Is vegan"


class VegetarianFilterForm(forms.Form):
    vegetarian = forms.BooleanField(required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["vegetarian"].label = "Is vegetarian"


class CountryFilterForm(forms.Form):
    country = forms.ModelChoiceField(queryset=Country.objects.all(), required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["country"].label = "Country"


class DifficultyLevelFilterForm(forms.Form):
    level = forms.ModelChoiceField(
        queryset=DifficultyLevel.objects.all(), required=False
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["level"].label = "Difficulty Level"


class CategoryFilterForm(forms.Form):
    category = forms.ModelChoiceField(
        queryset=DishCategory.objects.all(), required=False
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["category"].label = "Category"
