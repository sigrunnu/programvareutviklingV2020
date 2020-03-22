# Generated by Django 3.0.3 on 2020-03-20 18:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('feed', '0004_auto_20200320_1925'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rating',
            name='user',
            field=models.ForeignKey(
                limit_choices_to=models.Q(
                    profile__is_pro=True),
                on_delete=django.db.models.deletion.CASCADE,
                related_name='user_in_rating',
                to=settings.AUTH_USER_MODEL),
        ),
    ]