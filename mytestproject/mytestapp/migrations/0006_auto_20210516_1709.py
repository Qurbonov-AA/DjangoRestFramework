# Generated by Django 3.2.2 on 2021-05-16 12:09

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mytestapp', '0005_auto_20210516_1702'),
    ]

    operations = [
        migrations.AddField(
            model_name='answers',
            name='text_q',
            field=models.CharField(max_length=255, null=True, verbose_name='свой ответ на вопрос'),
        ),
        migrations.AlterField(
            model_name='answers',
            name='dates',
            field=models.DateField(default=datetime.datetime(2021, 5, 16, 17, 9, 58, 146983)),
        ),
        migrations.AlterField(
            model_name='answers',
            name='question',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='mytestapp.questions'),
        ),
        migrations.AlterField(
            model_name='interviews',
            name='bdate',
            field=models.DateField(default=datetime.datetime(2021, 5, 16, 17, 9, 58, 145985), verbose_name='дата старта'),
        ),
    ]