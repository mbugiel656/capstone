# Generated by Django 3.1 on 2020-10-05 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weatherdata', '0002_remove_currentweather_measurement_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='currentweather',
            name='measurement_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]