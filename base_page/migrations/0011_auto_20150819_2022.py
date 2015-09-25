# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base_page', '0010_auto_20150819_2020'),
    ]

    operations = [
        migrations.AlterField(
            model_name='moddate',
            name='current_date',
            field=models.DateTimeField(),
        ),
    ]
