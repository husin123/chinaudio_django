# Generated by Django 2.2.2 on 2020-07-02 02:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('target', '0003_remove_clip_src'),
    ]

    operations = [
        migrations.AddField(
            model_name='clip',
            name='src',
            field=models.CharField(default='', max_length=255),
        ),
    ]
