# Generated by Django 2.2.2 on 2020-04-19 09:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ocr', '0008_auto_20200419_0920'),
    ]

    operations = [
        migrations.RenameField(
            model_name='chineseelem',
            old_name='desc',
            new_name='desc_info',
        ),
    ]