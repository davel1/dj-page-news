# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base_page', '0013_auto_20150824_1715'),
    ]

    operations = [
        migrations.AlterField(
            model_name='honors',
            name='photo',
            field=models.ImageField(upload_to=b'honors'),
        ),
    ]
