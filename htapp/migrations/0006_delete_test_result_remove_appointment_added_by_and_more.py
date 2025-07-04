# Generated by Django 4.0.5 on 2022-06-13 05:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('htapp', '0005_laboratory_feed_back'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Test_result',
        ),
        migrations.RemoveField(
            model_name='appointment',
            name='Added_by',
        ),
        migrations.RemoveField(
            model_name='appointment',
            name='Added_date_time',
        ),
        migrations.RemoveField(
            model_name='appointment',
            name='Updated_by',
        ),
        migrations.RemoveField(
            model_name='appointment',
            name='Updated_date_time',
        ),
        migrations.AlterField(
            model_name='person',
            name='Person_gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('M', 'Male'), ('O', 'Other')], default='M', max_length=1, verbose_name='Gender'),
        ),
        migrations.AlterField(
            model_name='person',
            name='Person_rating',
            field=models.CharField(choices=[('1', '*'), ('2', '**'), ('3', '***'), ('4', '****'), ('5', '*****')], default=5, max_length=1, verbose_name='Rating'),
        ),
        migrations.AlterField(
            model_name='person',
            name='Person_status',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='health status'),
        ),
    ]
