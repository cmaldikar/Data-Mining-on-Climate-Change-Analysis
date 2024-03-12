# Generated by Django 4.2.6 on 2023-12-05 00:28

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="TemperaturePrediction",
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
                ("city", models.CharField(max_length=255)),
                ("year", models.IntegerField()),
                ("month", models.IntegerField()),
                ("max_temperature", models.FloatField()),
                ("min_temperature", models.FloatField()),
                ("city_prediction", models.CharField(max_length=255)),
            ],
        ),
    ]
