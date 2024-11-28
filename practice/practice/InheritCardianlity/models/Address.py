from django.db import models


class Address(models.Model):
    area = models.CharField(max_length=50)
    street = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    pin_code = models.PositiveIntegerField()


    class Meta:
        abstract = True
