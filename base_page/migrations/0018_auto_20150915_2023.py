# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('base_page', '0017_auto_20150915_1931'),
    ]

    operations = [
        migrations.AlterField(
            model_name='honors',
            name='description',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
