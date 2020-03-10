# Generated by Django 3.0.3 on 2020-03-10 07:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0005_auto_20200310_0835'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exercise',
            name='exerciseImage',
            field=models.ImageField(blank=True, null=True, upload_to='exercises/', verbose_name='Bilde av øvelsen'),
        ),
        migrations.AlterField(
            model_name='exercise',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 10, 8, 43, 2, 182006), editable=False),
        ),
    ]
