# Generated by Django 2.2.2 on 2020-07-02 09:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('target', '0004_clip_src'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='algorithmsmediums',
            name='medium',
        ),
    ]