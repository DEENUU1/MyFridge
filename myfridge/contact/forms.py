from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    accept_statute = forms.BooleanField()

    class Meta:
        model = Contact
        fields = ("username", "email", "subject", "message")
