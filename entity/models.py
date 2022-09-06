from django.db import models
from company.models import Company

class Entity(models.Model):
    name = models.CharField(max_length=255)
    document = models.CharField(max_length=25)
    active = models.BooleanField(default=True)
    inicio_contrato = models.DateTimeField(null=True, blank=True, default='')
    fim_contrato = models.DateTimeField(null=True, blank=True, default='')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    company = models.ForeignKey(Company, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name
