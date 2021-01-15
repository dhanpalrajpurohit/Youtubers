# Generated by Django 3.1.5 on 2021-01-15 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('youtubers', '0006_auto_20210115_1102'),
    ]

    operations = [
        migrations.AlterField(
            model_name='youtuber',
            name='camera_type',
            field=models.CharField(choices=[('nikon', 'Nikon'), ('sony', 'Sony'), ('canan', 'Canan')], max_length=255),
        ),
        migrations.AlterField(
            model_name='youtuber',
            name='category',
            field=models.CharField(choices=[('coding', 'Coding'), ('gaming', 'Gaming'), ('health', 'Health')], max_length=255),
        ),
        migrations.AlterField(
            model_name='youtuber',
            name='crew',
            field=models.CharField(choices=[('large', 'Large'), ('solo', 'Solo'), ('dute', 'Dute'), ('small', 'Small')], max_length=255),
        ),
    ]