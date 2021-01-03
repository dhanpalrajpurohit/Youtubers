# Generated by Django 3.1.4 on 2021-01-02 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('youtubers', '0002_auto_20210101_1538'),
    ]

    operations = [
        migrations.AddField(
            model_name='youtuber',
            name='video_url',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='youtuber',
            name='camera_type',
            field=models.CharField(choices=[('sony', 'Sony'), ('nikon', 'Nikon'), ('canan', 'Canan')], max_length=255),
        ),
        migrations.AlterField(
            model_name='youtuber',
            name='category',
            field=models.CharField(choices=[('coding', 'Coding'), ('health', 'Health'), ('gaming', 'Gaming')], max_length=255),
        ),
        migrations.AlterField(
            model_name='youtuber',
            name='crew',
            field=models.CharField(choices=[('small', 'Small'), ('solo', 'Solo'), ('dute', 'Dute'), ('large', 'Large')], max_length=255),
        ),
    ]
