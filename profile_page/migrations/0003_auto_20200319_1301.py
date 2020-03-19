# Generated by Django 3.0.3 on 2020-03-19 12:01

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('profile_page', '0002_createdby'),
    ]

    operations = [
        migrations.AlterField(
            model_name='createdby',
            name='user',
            field=models.ForeignKey(
                blank=True, null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL),
        ),
    ]
