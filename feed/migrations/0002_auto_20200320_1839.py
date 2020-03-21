# Generated by Django 3.0.3 on 2020-03-20 17:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('feed', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='exercise',
            options={'ordering': ['exercise_title']},
        ),
        migrations.RenameField(
            model_name='exercise',
            old_name='createdBy',
            new_name='created_by',
        ),
        migrations.RenameField(
            model_name='exercise',
            old_name='exerciseHowTo',
            new_name='exercise_how_to',
        ),
        migrations.RenameField(
            model_name='exercise',
            old_name='exerciseImage',
            new_name='exercise_image',
        ),
        migrations.RenameField(
            model_name='exercise',
            old_name='exerciseInfo',
            new_name='exercise_info',
        ),
        migrations.RenameField(
            model_name='exercise',
            old_name='exerciseTitle',
            new_name='exercise_title',
        ),
        migrations.RenameField(
            model_name='exercise',
            old_name='muscleGroup',
            new_name='muscle_group',
        ),
        migrations.RenameField(
            model_name='musclegroup',
            old_name='muscleGroupTitle',
            new_name='muscle_group_title',
        ),
        migrations.RemoveField(
            model_name='exercise',
            name='isPublic',
        ),
        migrations.AddField(
            model_name='exercise',
            name='is_public',
            field=models.BooleanField(
                default=False,
                verbose_name='Offentlig for ikke registrerte brukere'),
        ),
        migrations.AlterField(
            model_name='exercise',
            name='favorisations',
            field=models.ManyToManyField(
                blank=True,
                related_name='favorisations',
                through='feed.Favorisation',
                to=settings.AUTH_USER_MODEL,
                verbose_name='Favoriseringer'),
        ),
        migrations.AlterField(
            model_name='favorisation',
            name='exercise',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name='exercise_in_favorisation', to='feed.Exercise'),
        ),
        migrations.AlterField(
            model_name='favorisation',
            name='user',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name='user_in_favorisation',
                to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(
                    auto_created=True,
                    primary_key=True,
                    serialize=False,
                    verbose_name='ID')),
                ('rating_number', models.IntegerField(
                    choices=[
                        (1, 'Very low'),
                        (2, 'Low'),
                        (3, 'Normal'),
                        (4, 'High'),
                        (5, 'Very high')
                    ])),
                ('exercise', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE,
                    related_name='exercise_in_rating', to='feed.Exercise')),
                ('user', models.ForeignKey(
                    limit_choices_to={'profile.is_pro': True},
                    on_delete=django.db.models.deletion.CASCADE,
                    related_name='user_in_rating',
                    to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='exercise',
            name='ratings',
            field=models.ManyToManyField(
                blank=True,
                related_name='ratings',
                through='feed.Rating',
                to=settings.AUTH_USER_MODEL, verbose_name='Rangering'),
        ),
    ]
