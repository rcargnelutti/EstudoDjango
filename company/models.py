from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=255)
    document = models.CharField(max_length=25)
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Entity(models.Model):
    name = models.CharField(max_length=255)
    document = models.CharField(max_length=25)
    active = models.BooleanField(default=True)
    inicio_contrato = models.DateTimeField()
    fim_contrato = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


