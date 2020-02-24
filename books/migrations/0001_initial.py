# Generated by Django 3.0.3 on 2020-02-22 14:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('salutation', models.CharField(max_length=10)),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('headshot', models.ImageField(blank=True, null=True, upload_to='authors')),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('address', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=60)),
                ('state_province', models.CharField(max_length=30)),
                ('country', models.CharField(max_length=50)),
                ('website', models.URLField()),
                ('latitude', models.DecimalField(blank=True, decimal_places=15, default=0, max_digits=19, null=True)),
                ('longitude', models.DecimalField(blank=True, decimal_places=15, default=0, max_digits=19, null=True)),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, unique=True)),
            ],
            options={
                'verbose_name': 'Tag',
                'verbose_name_plural': 'Tags',
            },
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, null=True)),
                ('summary', models.TextField(blank=True, null=True)),
                ('publication_date', models.DateField()),
                ('state', models.CharField(choices=[('published', 'Published'), ('not_published', 'Not published'), ('in_progress', 'In progress'), ('cancelled', 'Cancelled'), ('rejected', 'Rejected')], default='published', max_length=100)),
                ('isbn', models.CharField(max_length=100, unique=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('pages', models.PositiveIntegerField(default=200)),
                ('stock_count', models.PositiveIntegerField(default=30)),
                ('authors', models.ManyToManyField(related_name='books', to='books.Author')),
                ('publisher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='books', to='books.Publisher')),
                ('tags', models.ManyToManyField(blank=True, related_name='books', to='books.Tag')),
            ],
            options={
                'ordering': ['isbn'],
            },
        ),
    ]
