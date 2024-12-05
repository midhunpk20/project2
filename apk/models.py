from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=80)
    phone_number = models.CharField(max_length=13)
    location = models.CharField(max_length=255)


