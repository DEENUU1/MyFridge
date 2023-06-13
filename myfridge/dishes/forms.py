from django import forms
from .models import (
    Country,
    DifficultyLevel,
    DishCategory,
    MainIngredient,
)
from django.urls import reverse
from users.task import send_email_task


class MainIngredientForm(forms.Form):
    ingredients = forms.ModelMultipleChoiceField(
        queryset=MainIngredient.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
    )


class DateSortingForm(forms.Form):
    CHOICES = (("1", "Newest"), ("2", "Oldest"))

    order_by = forms.ChoiceField(
        choices=CHOICES,
        required=False,
    )


class CaloriesSortingForm(forms.Form):
    CHOICES = (("1", "Highest"), ("2", "Lowest"))

    order_by = forms.ChoiceField(
        choices=CHOICES,
        required=False,
    )


class SearchForm(forms.Form):
    search_query = forms.CharField(
        label="Search",
        max_length=100,
        required=False,
        widget=forms.TextInput(attrs={"placeholder": "Search for dishes"}),
    )


class TimeToMake(forms.Form):
    CHOICES = (("1", "Shortest"), ("2", "Longest"))

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


class SendIngredientForm(forms.Form):
    email = forms.EmailField(label="Your email address")
    accept_statute = forms.BooleanField()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['accept_statute'].help_text = f'<a href="{reverse("contact:contact-statute")}">Read the statute</a>'

    def send_email(self, message):
        send_email_task.delay(
            self.cleaned_data.get("email"),
            subject="List of ingredients",
            message=message
        )
