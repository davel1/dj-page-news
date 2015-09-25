# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base_page', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='stud_full_name',
            field=models.CharField(default=1, max_length=120),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='myuser',
            name='student',
            field=models.BooleanField(default=False),
        ),
    ]
