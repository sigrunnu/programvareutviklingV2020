# Generated by Django 3.0.3 on 2020-03-22 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0005_auto_20200320_1926'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exercise',
            name='exercise_image',
            field=models.ImageField(blank=True, default='exercises/mark_EtbcZQP.jpg.250x250_q85_crop_detail.jpg.jpg', null=True, upload_to='exercises/', verbose_name='Bilde av øvelsen'),
        ),
    ]
