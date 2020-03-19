# Generated by Django 3.0.3 on 2020-03-19 10:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='MuscleGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('muscleGroupTitle', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Exercise',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exerciseTitle', models.CharField(max_length=200, verbose_name='Tittel på øvelsen')),
                ('exerciseInfo', models.TextField(blank=True, max_length=500, null=True, verbose_name='Informasjon om øvelsen')),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
                ('exerciseLikes', models.IntegerField(default=0)),
                ('exerciseRating', models.DecimalField(blank=True, decimal_places=3, max_digits=4, null=True)),
                ('exerciseHowTo', models.TextField(blank=True, max_length=500, null=True, verbose_name='Utførelse av øvelsen')),
                ('exerciseImage', models.ImageField(blank=True, null=True, upload_to='exercises/', verbose_name='Bilde av øvelsen')),
                ('createdBy', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('muscleGroup', models.ManyToManyField(blank=True, to='feed.MuscleGroup', verbose_name='Muskelgrupper')),
            ],
            options={
                'ordering': ['exerciseLikes', 'exerciseRating', 'exerciseTitle'],
            },
        ),
    ]
