# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Role',
            fields=[
                ('role_id', models.CharField(max_length=10, serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=20)),
                ('last_updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.CharField(max_length=20, serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=100)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('role_id', models.ForeignKey(to='users.Role')),
            ],
        ),
    ]
