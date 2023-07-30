# Generated by Django 4.2.3 on 2023-07-25 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctors', '0002_alter_doctor_non_reimbursement_subjects'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='non_reimbursement_subjects',
            field=models.ManyToManyField(blank=True, related_name='doctors', to='doctors.nonreimbursementdepartment'),
        ),
    ]
