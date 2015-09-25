# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base_page', '0007_auto_20150819_1624'),
    ]

    operations = [
        migrations.CreateModel(
            name='ModDate',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('current_date', models.DateField()),
                ('mod', models.BooleanField()),
            ],
        ),
    ]
