# Generated by Django 3.1 on 2020-11-27 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weatherdata', '0008_auto_20201124_2113'),
    ]

    operations = [
        migrations.AlterField(
            model_name='currentweather',
            name='temperature',
            field=models.IntegerField(blank=True, default=0, verbose_name='Temperature (C)'),
        ),
    ]