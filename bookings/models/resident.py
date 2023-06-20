from django.db import models

from utils.validators import phone_validator


class Resident(models.Model):
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=15, validators=[phone_validator], null=True)
    email = models.EmailField(null=True)

    def __str__(self):
        return self.name
