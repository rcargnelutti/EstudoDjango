# Generated by Django 4.1.1 on 2022-09-05 20:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0004_alter_entity_fim_contrato_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entity',
            name='fim_contrato',
            field=models.DateTimeField(blank=True),
        ),
        migrations.AlterField(
            model_name='entity',
            name='inicio_contrato',
            field=models.DateTimeField(blank=True),
        ),
    ]
