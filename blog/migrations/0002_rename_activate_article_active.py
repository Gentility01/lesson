# Generated by Django 3.2.9 on 2021-12-15 03:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='activate',
            new_name='active',
        ),
    ]
