# Generated by Django 3.2 on 2021-04-12 10:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fsblog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='compile',
            new_name='complete',
        ),
    ]