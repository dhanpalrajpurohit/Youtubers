# Generated by Django 3.1.5 on 2021-01-15 11:02

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hiretuber', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hiretuber',
            name='created_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 1, 15, 11, 2, 9, 603173)),
        ),
    ]
