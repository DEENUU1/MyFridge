from django.db import models


class ContactSubject(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Contact(models.Model):
    username = models.CharField(max_length=50)
    date_created = models.DateTimeField(auto_now_add=True)
    email = models.EmailField()
    subject = models.ForeignKey(ContactSubject, on_delete=models.CASCADE)
    message = models.CharField(max_length=500)

    def __str__(self):
        return self.username
