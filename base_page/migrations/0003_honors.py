# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('base_page', '0002_auto_20150817_2118'),
    ]

    operations = [
        migrations.CreateModel(
            name='Honors',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('photo', models.FileField(upload_to=b'honors')),
                ('article', models.CharField(max_length=60)),
                ('description', models.TextField()),
                ('date_event', models.DateTimeField()),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
