# Generated by Django 3.2.7 on 2021-10-24 12:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_delete_favoritenews'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='publication',
            name='short_description',
        ),
    ]
