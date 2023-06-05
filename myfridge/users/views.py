from django import views
from django.contrib.auth import login, logout
from django.contrib.auth.views import LogoutView
from django.contrib.sites.shortcuts import get_current_site
from django.http import HttpResponse, HttpRequest
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.views.generic import UpdateView, TemplateView, CreateView
from django.views.generic.edit import FormView
from dotenv import load_dotenv
from .models import CustomUser

from .forms import (
    CustomUserRegistration,
    CustomUserLogin,
    ChangePasswordForm,
    DeleteAccountForm,
)

from .tokens import account_activation_token
from social.models import Feedback

load_dotenv()


class RegisterUserView(FormView):
    form_class = CustomUserRegistration
    template_name = "register.html"
    success_url = reverse_lazy("users:success_register")

    def form_valid(self, form):
        user = form.save(commit=False)
        user.is_active = False
        user.set_password(form.cleaned_data["password"])
        user.save()
        # TODO send email method

        return super().form_valid(form)


def send_activation_url(request: HttpRequest, uidb64: str, token: str) -> HttpResponse:
    """
    The function register_activate() takes in three arguments:
    - request: the request object sent by the user to activate their account
    - idb64: the unique identifier in base64 encoded format
    - token: the token sent in the activation link
    The function attempts to decode the idb64 value and retrieve the corresponding user from the database.
    If the user is found and the token is valid, the user's account is activated, they are logged in,
    and a success message is returned. If the user is not found or the token is invalid, an error message is returned.
    Returns:
        - HttpResponse: A success or error message to be displayed to the user upon attempting to activate their account
    """
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = CustomUser.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, CustomUser.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        return HttpResponse(
            "Thank you for your email confirmation. Now you can login your account."
        )
    else:
        return HttpResponse("Activation link is invalid!")


class SuccessRegisterView(TemplateView):
    template_name = "success_register.html"


class StatuteView(TemplateView):
    template_name = "statute.html"


class LoginUserView(FormView):
    template_name = "login.html"
    form_class = CustomUserLogin
    success_url = reverse_lazy("dishes:home")

    def form_valid(self, form):
        """
        Overrides the parent class method to log the user in upon successful
        authentication and redirect them to the success URL.
        """
        login(self.request, form.get_user())
        return super().form_valid(form)


class LogoutUserView(LogoutView):
    def get(self, request):
        logout(request)
        return redirect("dishes:home")


class ChangePasswordView(FormView):
    form_class = ChangePasswordForm
    template_name = "change_password.html"
    success_url = reverse_lazy("users:success_password_change")

    def form_valid(self, form):  # TODO move this logic to form
        try:
            user = CustomUser.objects.get(email=form.cleaned_data["email"])
        except CustomUser.DoesNotExist:
            form.add_error(None, "User with this email does not exist")
            return super().form_invalid(form)

        if not user.check_password(form.cleaned_data["old_password"]):
            form.add_error("old_password", "Old password is incorrect")
            return super().form_invalid(form)

        user.set_password(form.cleaned_data["new_password"])
        user.is_active = False
        user.save()
        # TODO send email method

        return super().form_valid(form)


class SuccessPasswordChangeView(TemplateView):
    template_name = "password_change_success.html"


class DeleteAccountView(FormView):
    form_class = DeleteAccountForm
    template_name = "delete_account.html"
    success_url = reverse_lazy("users:success_delete_account")

    def form_valid(self, form):  # TODO move this logic to form
        try:
            user = CustomUser.objects.get(email=form.cleaned_data["email"])
        except CustomUser.DoesNotExist:
            form.add_error(None, "User with this email does not exist")
            return super().form_invalid(form)

        if not user.check_password(form.cleaned_data["password"]):
            form.add_error("password", "Password is incorrect")
            return super().form_invalid(form)

        user.delete()
        # TODO send email method

        return super().form_valid(form)


class SuccessDeleteAccountView(CreateView):
    template_name = "delete_account_success.html"
    model = Feedback
    fields = ("message",)
    success_url = reverse_lazy("dishes:home")
