# Generated by Django 4.0.5 on 2022-08-19 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('htapp', '0019_alter_result_test_name_test'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pharmacy',
            name='Pharmacy_name',
            field=models.CharField(max_length=100, null=True, verbose_name='PHARMACY NAME'),
        ),
    ]
