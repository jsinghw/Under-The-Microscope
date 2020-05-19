from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class CustomUser(AbstractUser):
    display_name = models.CharField(max_length=50, null=True)

    REQUIRED_FIELDS = ['display_name']
