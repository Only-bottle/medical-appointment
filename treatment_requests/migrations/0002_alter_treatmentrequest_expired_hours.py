# Generated by Django 4.2.3 on 2023-07-31 14:05

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("treatment_requests", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="treatmentrequest",
            name="expired_hours",
            field=models.DateTimeField(blank=True),
        ),
    ]
