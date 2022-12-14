# Generated by Django 4.1.1 on 2022-09-12 15:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("entity", "0005_alter_entity_company"),
    ]

    operations = [
        migrations.CreateModel(
            name="Unity",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255)),
                ("fraction", models.CharField(max_length=25)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "entity",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="entity.entity"
                    ),
                ),
            ],
        ),
    ]
