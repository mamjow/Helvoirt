from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):

    # add additional fields in here
    Birth_date = models.DateField(null=True)

    def __str__(self):
        return self.username

