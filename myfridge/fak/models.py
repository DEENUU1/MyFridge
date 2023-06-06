from django.db import models

import datetime


class Fak(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Medicine(models.Model):
    QUANTITY = (("LOW", "LOW"), ("MEDIUM", "MEDIUM"), ("HIGH", "HIGH"))

    name = models.CharField(max_length=50)
    expiration_date = models.DateField()
    quantity = models.CharField(max_length=10, choices=QUANTITY)
    fak = models.ForeignKey(Fak, on_delete=models.CASCADE)

    @property
    def get_expiration_date_info(self):
        if self.expiration_date < datetime.datetime.now().date():
            return "Expired"
        elif (
            self.expiration_date
            < (datetime.datetime.now() + datetime.timedelta(days=7)).date()
        ):
            return "Attention, expiration date is coming soon"
        else:
            return str(self.expiration_date)

    def __str__(self):
        return self.name
