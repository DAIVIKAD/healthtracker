# Generated by Django 4.0.5 on 2022-08-19 16:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('htapp', '0033_alter_appointment_appointment_time_duration'),
    ]

    operations = [
        migrations.RenameField(
            model_name='appointment',
            old_name='Appointment_time_duration',
            new_name='Appointment_time_dur',
        ),
    ]
