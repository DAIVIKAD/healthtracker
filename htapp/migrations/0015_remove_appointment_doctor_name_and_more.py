# Generated by Django 4.0.5 on 2022-08-19 13:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('htapp', '0014_remove_appointment_person_name_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appointment',
            name='Doctor_name',
        ),
        migrations.AddField(
            model_name='appointment',
            name='Docter_name',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='htapp.person', verbose_name='PERSON NAME'),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='Person_name',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='DOCTER NAME'),
        ),
    ]
