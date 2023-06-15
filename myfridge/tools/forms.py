from django import forms


class CaloricNeedsForm(forms.Form):
    weight = forms.FloatField(label="Weight", required=True)
    height = forms.IntegerField(label="Height", required=True)
    age = forms.IntegerField(label="Age", required=True)
    gender = forms.ChoiceField(label="Gender", choices=(("M", "Male"), ("F", "Female")), required=True)
    ACTIVITY_CHOICES = (
        (1.2, "Brak aktywności zawodowej, chory, leżący"),
        (1.4, "Pracownik biurowy, którego aktywność związana jest wyłącznie z obowiązkami domowymi"),
        (1.6, "Pracownik biurowy, trenujący 2-3 razy w tygodniu przez minimum godzinę"),
        (1.8, "Pracownik biurowy, trenujący 3-4 razy w tygodniu przez minimum godzinę"),
        (2.0, "Zawodowy sportowiec, trenujący minimum 6 godzin tygodniowo lub osoba ciężko pracująca fizycznie")
    )
    activity = forms.ChoiceField(label="Activity", choices=ACTIVITY_CHOICES, required=True)

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
        return f"{int(caloric_needs)} kcal. This is your caloric needs to stay healthy"


class PerfectWeightForm(forms.Form):
    height = forms.IntegerField(label="Height", required=True)

    def calculate_perfect_weight(self) -> float | int:
        cleaned_data = super().clean()
        height = cleaned_data.get("height")
        MIN_BMI = 18.5
        MAX_BMI = 24.9

        min_perfect_weight = MIN_BMI * (height * height)
        max_perfect_weight = MAX_BMI * (height * height)

        return min_perfect_weight, max_perfect_weight


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
