from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import CustomUser


class CustomUserRegistration(forms.ModelForm):

    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password_repeat = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = CustomUser
        fields = (
            "username",
            "email",
            "password",
            "password_repeat"
        )

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if CustomUser.objects.filter(email=email).exists():
            raise forms.ValidationError("Email already exists")
        return email

    def clean_password_repeat(self):
        password = self.cleaned_data.get("password")
        password_repeat = self.cleaned_data.get("password_repeat")
        if password != password_repeat:
            raise forms.ValidationError("Passwords don't match")
        return password_repeat

    def send_email(self, message):
        pass


class CustomUserLogin(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
