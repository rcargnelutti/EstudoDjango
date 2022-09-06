from django.contrib import admin

from company.models import Company, Entity

# Register your models here.
admin.site.register(Company)
admin.site.register(Entity)