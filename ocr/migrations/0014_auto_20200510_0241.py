# Generated by Django 2.2.2 on 2020-05-10 02:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ocr', '0013_auto_20200502_2129'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='polygonelem',
            unique_together={('polygon', 'elem', 'create_user_id')},
        ),
    ]
