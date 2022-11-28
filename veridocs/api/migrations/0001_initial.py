# Generated by Django 4.1.3 on 2022-11-28 03:10

import api.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('uid', models.CharField(max_length=30, unique=True)),
                ('id', models.CharField(default=api.models.key_generator, editable=False, max_length=6, primary_key=True, serialize=False, unique=True)),
            ],
        ),
    ]
