# Generated by Django 3.2.2 on 2021-06-12 11:53

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mytestapp', '0007_auto_20210530_1729'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answers',
            name='user',
        ),
        migrations.AddField(
            model_name='answers',
            name='username',
            field=models.CharField(default='None', max_length=255, verbose_name='username'),
        ),
        migrations.AlterField(
            model_name='answers',
            name='dates',
            field=models.DateField(default=datetime.datetime(2021, 6, 12, 16, 53, 43, 344464)),
        ),
        migrations.AlterField(
            model_name='interviews',
            name='bdate',
            field=models.DateField(default=datetime.datetime(2021, 6, 12, 16, 53, 43, 343435), verbose_name='дата старта'),
        ),
        migrations.AlterField(
            model_name='questions',
            name='interview',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='question', to='mytestapp.interviews'),
        ),
    ]
