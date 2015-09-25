# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import redactor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('base_page', '0015_myuser_boss'),
    ]

    operations = [
        migrations.AlterField(
            model_name='honors',
            name='description',
            field=redactor.fields.RedactorField(verbose_name='Text'),
        ),
    ]
