# Generated by Django 3.2.7 on 2021-10-23 17:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='FavoriteNews',
        ),
    ]