# Generated by Django 2.2.2 on 2019-12-31 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_pitchuser_session'),
    ]

    operations = [
        migrations.AddField(
            model_name='pitchuser',
            name='login_ip',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
