# Generated by Django 4.0.5 on 2022-08-26 05:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('htapp', '0042_remove_pharmacy_pharmacy_item'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='Appointment_duration',
            field=models.DurationField(blank=True, max_length=100, null=True, verbose_name=' DURATION'),
        ),
    ]
