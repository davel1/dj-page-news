# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='quote',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('q', models.TextField()),
                ('q_date', models.DateTimeField(verbose_name=b'data quote')),
                ('r', models.TextField()),
                ('r_date', models.DateTimeField(verbose_name=b'data request')),
                ('public', models.BooleanField()),
            ],
        ),
    ]
