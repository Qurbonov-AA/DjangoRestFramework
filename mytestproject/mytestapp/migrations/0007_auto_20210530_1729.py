# Generated by Django 3.2.2 on 2021-05-30 12:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mytestapp', '0006_auto_20210516_1709'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='answers',
            options={'verbose_name': 'Ответ', 'verbose_name_plural': 'Ответы'},
        ),
        migrations.AlterField(
            model_name='answers',
            name='dates',
            field=models.DateField(default=datetime.datetime(2021, 5, 30, 17, 29, 48, 708663)),
        ),
        migrations.AlterField(
            model_name='interviews',
            name='bdate',
            field=models.DateField(default=datetime.datetime(2021, 5, 30, 17, 29, 48, 708163), verbose_name='дата старта'),
        ),
    ]