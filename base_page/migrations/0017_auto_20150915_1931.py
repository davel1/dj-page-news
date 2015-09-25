# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base_page', '0016_auto_20150915_1917'),
    ]

    operations = [
        migrations.AlterField(
            model_name='honors',
            name='description',
            field=models.TextField(),
        ),
    ]
