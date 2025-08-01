from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('user', 'User'),
        ('provider', 'Service Provider'),
        ('admin', 'Admin'),
    )
    full_name = models.CharField(max_length=100)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)
    address = models.TextField(blank=True, null=True)
    contact_number = models.CharField(max_length=10, blank=True, null=True)
    is_approved = models.BooleanField(default=False)  # Admin approval