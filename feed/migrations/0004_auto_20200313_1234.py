# Generated by Django 3.0.3 on 2020-03-13 12:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0003_auto_20200309_1105'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='exercise',
            name='createdByPro',
        ),
        migrations.RemoveField(
            model_name='exercise',
            name='cropping',
        ),
    ]
