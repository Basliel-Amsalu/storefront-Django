# Generated by Django 5.0.4 on 2024-04-11 15:28

import django.db.models.manager
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tags', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='taggeditem',
            managers=[
                ('object', django.db.models.manager.Manager()),
            ],
        ),
    ]