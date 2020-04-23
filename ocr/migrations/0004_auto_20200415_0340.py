# Generated by Django 2.2.2 on 2020-04-15 03:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ocr', '0003_imageuserconf_filter_size'),
    ]

    operations = [
        migrations.AddField(
            model_name='imageuserconf',
            name='center_x',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='imageuserconf',
            name='center_y',
            field=models.FloatField(default=0.2),
        ),
        migrations.AddField(
            model_name='imageuserconf',
            name='room_scale',
            field=models.FloatField(default=1),
        ),
    ]