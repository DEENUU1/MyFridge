from django.views.generic import FormView, TemplateView
from .forms import ContactForm
from django.urls import reverse_lazy


class ContactFormView(FormView):
    template_name = "contact.html"
    form_class = ContactForm
    success_url = reverse_lazy("contact:contact-success")

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class ContactSuccessView(TemplateView):
    template_name = "contact_success.html"


class ContactStatueView(TemplateView):
    template_name = "contact_statue.html"
