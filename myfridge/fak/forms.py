from django import forms
from django.urls import reverse


class SendIngredientForm(forms.Form):
    email = forms.EmailField(label="Your email address")
    accept_statute = forms.BooleanField()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['accept_statute'].help_text = f'<a href="{reverse("contact:contact-statute")}">Read the statute</a>'
