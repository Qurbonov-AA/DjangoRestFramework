# Generated by Django 3.2.2 on 2021-05-09 11:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='interviews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('iname', models.CharField(max_length=255, verbose_name='Intervyular nomlari')),
                ('bdate', models.DateField(default=datetime.datetime(2021, 5, 9, 16, 54, 35, 941723))),
                ('edate', models.DateField()),
                ('description', models.TextField()),
            ],
        ),
    ]
