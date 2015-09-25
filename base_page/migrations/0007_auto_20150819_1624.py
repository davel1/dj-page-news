# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base_page', '0006_honors_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='honors',
            name='user',
        ),
        migrations.AddField(
            model_name='honors',
            name='student',
            field=models.ForeignKey(default=1, to='base_page.GroupList'),
            preserve_default=False,
        ),
    ]
