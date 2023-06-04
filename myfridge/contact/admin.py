from django.contrib import admin
from .models import Contact, ContactSubject


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    pass


@admin.register(ContactSubject)
class ContactSubjectAdmin(admin.ModelAdmin):
    pass
