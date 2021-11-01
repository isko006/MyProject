# Generated by Django 3.2.7 on 2021-10-23 17:08

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
            name='Law',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('short_description', models.TextField()),
                ('full_description', models.TextField()),
                ('publication_date', models.DateTimeField()),
                ('file', models.FileField(upload_to='files')),
                ('type', models.IntegerField(choices=[(1, 'Действуюшие законодательства'), (2, 'Проекты нормативных-правовых актов'), (3, 'Международные докумаенты')], default=1)),
            ],
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('short_description', models.TextField()),
                ('publication_date', models.DateTimeField()),
                ('full_description', models.TextField()),
                ('image', models.ImageField(null=True, upload_to='news')),
                ('link', models.URLField()),
                ('is_main', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Publication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('short_description', models.TextField()),
                ('full_description', models.TextField()),
                ('publication_date', models.DateTimeField()),
                ('file', models.FileField(upload_to='files')),
                ('type', models.IntegerField(choices=[(1, 'публикации IKNL'), (2, 'Другие публикации')], default=1)),
            ],
        ),
        migrations.CreateModel(
            name='ImageNews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='news')),
                ('news', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='news.news')),
            ],
        ),
        migrations.CreateModel(
            name='FavoriteNews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('news', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='news.news')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
