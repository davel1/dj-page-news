# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base_page', '0004_remove_honors_photo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='honors',
            name='user',
        ),
        migrations.AddField(
            model_name='honors',
            name='photo',
            field=models.FileField(default=1, upload_to=b'honors'),
            preserve_default=False,
        ),
    ]
