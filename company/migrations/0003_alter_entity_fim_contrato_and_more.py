# Generated by Django 4.1.1 on 2022-09-06 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0002_entity_company'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entity',
            name='fim_contrato',
            field=models.DateTimeField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='entity',
            name='inicio_contrato',
            field=models.DateTimeField(blank=True, default=''),
        ),
    ]
