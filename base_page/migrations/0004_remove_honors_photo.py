# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base_page', '0003_honors'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='honors',
            name='photo',
        ),
    ]
