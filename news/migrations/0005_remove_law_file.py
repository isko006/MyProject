# Generated by Django 3.2.7 on 2021-10-28 08:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_remove_publication_file'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='law',
            name='file',
        ),
    ]
