from django import forms


class DateSortingForm(forms.Form):
    CHOICES = (("1", "Newest"), ("2", "Oldest"))

    order_by = forms.ChoiceField(
        choices=CHOICES,
        required=False,
    )
