# Generated by Django 4.0.5 on 2022-08-19 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('htapp', '0028_alter_laboratory_pin_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='laboratory',
            name='Pin_code',
            field=models.CharField(blank=True, max_length=6, null=True, verbose_name='PIN CODE'),
        ),
    ]
