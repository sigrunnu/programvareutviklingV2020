# Generated by Django 3.0.3 on 2020-03-19 10:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='exercise',
            name='createdByPro',
        ),
    ]
