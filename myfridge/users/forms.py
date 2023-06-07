from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import CustomUser
from .task import send_email_task


class CustomUserRegistration(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={"class": "form-control"}))
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={"class": "form-control"})
    )
    password_repeat = forms.CharField(
        widget=forms.PasswordInput(attrs={"class": "form-control"})
    )
    accept_statute = forms.BooleanField()

    class Meta:
        model = CustomUser
        fields = ("username", "email", "password", "password_repeat")

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
        send_email_task.delay(
            self.cleaned_data.get("email"),
            subject="Activate your account",
            message=message
        )


class CustomUserLogin(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={"class": "form-control"})
    )


class ChangePasswordForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput)
    old_password = forms.CharField(widget=forms.PasswordInput)
    new_password = forms.CharField(widget=forms.PasswordInput)

    def send_email(self, message):
        send_email_task.delay(
            self.cleaned_data.get("email"),
            subject="Activate your account",
            message=message
        )


class DeleteAccountForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput)
    password = forms.CharField(widget=forms.PasswordInput)
    password_repeat = forms.CharField(widget=forms.PasswordInput)
