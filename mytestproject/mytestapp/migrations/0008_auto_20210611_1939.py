# Generated by Django 3.2.2 on 2021-06-11 14:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mytestapp', '0007_auto_20210530_1729'),
    ]

    operations = [
        migrations.AddField(
            model_name='answers',
            name='username',
            field=models.CharField(default='None', max_length=255, verbose_name='username'),
        ),
        migrations.AlterField(
            model_name='answers',
            name='dates',
            field=models.DateField(default=datetime.datetime(2021, 6, 11, 19, 39, 32, 259361)),
        ),
        migrations.AlterField(
            model_name='interviews',
            name='bdate',
            field=models.DateField(default=datetime.datetime(2021, 6, 11, 19, 39, 32, 257347), verbose_name='дата старта'),
        ),
    ]
