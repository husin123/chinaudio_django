# Generated by Django 2.2.2 on 2019-12-31 13:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0003_pitchuser_login_ip'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pitchuser',
            name='login_ip',
        ),
        migrations.RemoveField(
            model_name='pitchuser',
            name='session',
        ),
    ]
