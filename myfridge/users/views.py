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
from django.views.generic import UpdateView, TemplateView
from django.views.generic.edit import FormView
from dotenv import load_dotenv
from .models import CustomUser

from .forms import CustomUserRegistration, CustomUserLogin
from .tokens import account_activation_token

load_dotenv()


class RegisterUserView(FormView):
    form_class = CustomUserRegistration
    template_name = 'register.html'
    success_url = reverse_lazy('users:success_register')

    def form_valid(self, form):
        user = form.save(commit=False)
        user.is_active = False
        user.set_password(form.cleaned_data["password"])
        user.save()
        # send email method

        return super().form_valid(form)
