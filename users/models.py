from django.db import models
from django.contrib.auth.models import AbstractUser


class UserProfile(AbstractUser):

    email = models.EmailField(("email address"), unique=True)
    address = models.TextField(null=True, blank=True)
    phone = models.CharField(max_length=15, null=True, blank=True)

    def __str__(self) -> str:
        return self.email
