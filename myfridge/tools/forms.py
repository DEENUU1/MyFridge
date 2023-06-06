from django import forms


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
