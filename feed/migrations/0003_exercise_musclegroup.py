# Generated by Django 3.0.2 on 2020-02-12 10:29

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('feed', '0002_musclegroup'),
    ]

    operations = [
        migrations.AddField(
            model_name='exercise',
            name='muscleGroup',
            field=models.ManyToManyField(to='feed.MuscleGroup'),
        ),
    ]
