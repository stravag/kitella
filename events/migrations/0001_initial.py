# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-06 21:39
from __future__ import unicode_literals

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('firstname', models.CharField(max_length=200)),
                ('lastname', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='event',
            name='players',
            field=models.ManyToManyField(to='events.Player'),
        ),
    ]