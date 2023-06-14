from django import forms


class CaloriesCalculatorForm(forms.Form):
    weight = forms.FloatField(label="Weight", required=True)
    height = forms.IntegerField(label="Height", required=True)
    age = forms.IntegerField(label="Age", required=Ture)
    gender = forms.ChoiceField(label="Gender", choices=(("M", "Male"), ("F", "Female")), required=True)
    ACTIVITY_CHOICES = (
        (1.2, "Brak aktywności zawodowej, chory, leżący"),
        (1.4, "Pracownik biurowy, którego aktywność związana jest wyłącznie z obowiązkami domowymi"),
        (1.6, "Pracownik biurowy, trenujący 2-3 razy w tygodniu przez minimum godzinę"),
        (1.8, "Pracownik biurowy, trenujący 3-4 razy w tygodniu przez minimum godzinę"),
        (2.0, "Zawodowy sportowiec, trenujący minimum 6 godzin tygodniowo lub osoba ciężko pracująca fizycznie")
    )
    activity = forms.ChoiceField(label="Activity", choices=ACTIVITY_CHOICES, required=True)

    def calculate_calories(self) -> int:
        cleaned_data = super().clean()
        weight = cleaned_data.get("weight")
        height = cleaned_data.get("height")
        age = cleaned_data.get("age")
        gender = cleaned_data.get("gender")
        activity = float(cleaned_data.get("activity"))

        if gender == "M":
            return round(66 + (13.7 * weight) + (5 * height) - (6.8 * age) * activity)
        else:
            return round(655 + (9.6 * weight) + (1.8 * height) - (4.7 * age))


class BMIForm(forms.Form):
    weight = forms.FloatField(label="Weight")
    height = forms.IntegerField(label="Height")

    def calculate_bmi(self) -> float | None:
        cleaned_data = super().clean()
        weight = cleaned_data.get("weight")
        height = cleaned_data.get("height") / 100
        if weight is not None and height is not None:
            bmi = weight / (height * height)
            return round(bmi, 2)
        return None

    def return_bmi_result(self) -> str | None:
        bmi = self.calculate_bmi()
        if bmi is not None:
            if bmi < 18.5:
                return "Underweight"
            elif 18.5 <= bmi <= 24.9:
                return "Normal"
            elif 25 <= bmi <= 29.9:
                return "Overweight"
            else:
                return "Obese"
        return None
