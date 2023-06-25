from django import forms
from typing import Tuple
from .models import CaloricNeedsStatistics, PerfectWeightStatistics, BmiStatistics


class CaloricNeedsForm(forms.Form):
    weight = forms.FloatField(label="Weight", required=True)
    height = forms.IntegerField(label="Height", required=True)
    age = forms.IntegerField(label="Age", required=True)
    gender = forms.ChoiceField(
        label="Gender", choices=(("M", "Male"), ("F", "Female")), required=True
    )
    ACTIVITY_CHOICES = (
        (1.2, "Brak aktywności zawodowej, chory, leżący"),
        (
            1.4,
            "Pracownik biurowy, którego aktywność związana jest wyłącznie z obowiązkami domowymi",
        ),
        (1.6, "Pracownik biurowy, trenujący 2-3 razy w tygodniu przez minimum godzinę"),
        (1.8, "Pracownik biurowy, trenujący 3-4 razy w tygodniu przez minimum godzinę"),
        (
            2.0,
            "Zawodowy sportowiec, trenujący minimum 6 godzin tygodniowo lub osoba ciężko pracująca fizycznie",
        ),
    )
    activity = forms.ChoiceField(
        label="Activity", choices=ACTIVITY_CHOICES, required=True
    )

    def calculate_caloric_needs(self) -> float | int:
        cleaned_data = super().clean()
        weight = cleaned_data.get("weight")
        height = cleaned_data.get("height")
        age = cleaned_data.get("age")
        gender = cleaned_data.get("gender")
        activity = float(cleaned_data.get("activity"))

        if gender == "M":
            return (66 + (13.7 * weight) + (5 * height) - (6.8 * age)) * activity
        else:
            return (655 + (9.6 * weight) + (1.8 * height) - (4.7 * age)) * activity

    def return_caloric_needs(self) -> str | int:
        caloric_needs = self.calculate_caloric_needs()
        return f"{int(caloric_needs)}"

    def save_to_database(self):
        CaloricNeedsStatistics.objects.create(
            weight=self.cleaned_data.get("weight"),
            height=self.cleaned_data.get("height"),
            age=self.cleaned_data.get("age"),
            gender=self.cleaned_data.get("gender"),
            activity_level=self.cleaned_data.get("activity"),
            caloric_needs=self.calculate_caloric_needs(),
        )


class PerfectWeightForm(forms.Form):
    height = forms.IntegerField(label="Height", required=True)

    def calculate_perfect_weight(self) -> Tuple[float, float]:
        cleaned_data = super().clean()
        height = cleaned_data.get("height") / 100
        MIN_BMI = 18.5
        MAX_BMI = 24.9

        min_perfect_weight = MIN_BMI * (height * height)
        max_perfect_weight = MAX_BMI * (height * height)

        return round(min_perfect_weight, 2), round(max_perfect_weight, 2)

    def return_perfect_weight(self) -> str | int:
        min_perfect_weight, max_perfect_weight = self.calculate_perfect_weight()
        return f"Perfect weight should be between {min_perfect_weight} and {max_perfect_weight} kg."

    def save_to_database(self):
        PerfectWeightStatistics.objects.create(
            height=self.cleaned_data.get("height"),
            min_perfect_weight=self.calculate_perfect_weight()[0],
            max_perfect_weight=self.calculate_perfect_weight()[1],
        )


class BMIForm(forms.Form):
    weight = forms.FloatField(label="Weight", required=True)
    height = forms.IntegerField(label="Height", required=True)

    def calculate_bmi(self) -> float | None:
        cleaned_data = super().clean()
        weight = cleaned_data.get("weight")
        height = cleaned_data.get("height") / 100

        bmi = weight / (height * height)
        return round(bmi, 2)

    def return_bmi_result(self) -> str | None:
        bmi = self.calculate_bmi()

        if bmi < 18.5:
            return "Underweight"
        elif 18.5 <= bmi <= 24.9:
            return "Normal"
        elif 25 <= bmi <= 29.9:
            return "Overweight"
        else:
            return "Obese"

    def save_to_database(self):
        BmiStatistics.objects.create(
            weight=self.cleaned_data.get("weight"),
            height=self.cleaned_data.get("height"),
            bmi=self.calculate_bmi(),
        )
