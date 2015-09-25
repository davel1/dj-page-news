# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base_page', '0014_auto_20150824_1739'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='boss',
            field=models.BooleanField(default=False),
        ),
    ]
