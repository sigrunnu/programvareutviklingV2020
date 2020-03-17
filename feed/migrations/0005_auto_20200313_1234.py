# Generated by Django 3.0.3 on 2020-03-13 12:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profile_page', '0001_initial'),
        ('feed', '0004_auto_20200313_1234'),
    ]

    operations = [
        migrations.AddField(
            model_name='exercise',
            name='createdBy',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='profile_page.User', verbose_name='Bruker'),
        ),
        migrations.AlterField(
            model_name='exercise',
            name='exerciseImage',
            field=models.ImageField(blank=True, null=True, upload_to='exercises/', verbose_name='Bilde av øvelsen'),
        ),
        migrations.AlterField(
            model_name='exercise',
            name='pub_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
