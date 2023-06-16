from django import forms
from .models import Contact
from django.urls import reverse


class ContactForm(forms.ModelForm):
    accept_statute = forms.BooleanField()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields[
            "accept_statute"
        ].help_text = (
            f'<a href="{reverse("contact:contact-statute")}">Read the statute</a>'
        )

    class Meta:
        model = Contact
        fields = ("username", "email", "subject", "message")
