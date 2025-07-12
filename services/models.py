from django.db import models
from accounts.models import CustomUser

class ServiceCategory(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class ProviderService(models.Model):
    provider = models.ForeignKey(CustomUser, on_delete=models.CASCADE, limit_choices_to={'role': 'provider'})
    category = models.ForeignKey(ServiceCategory, on_delete=models.CASCADE)
    service_name = models.CharField(max_length=150)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True, null=True)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.service_name} - {self.provider.username}"
