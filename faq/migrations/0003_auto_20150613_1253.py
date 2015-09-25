# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('faq', '0002_auto_20150613_1233'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='public',
            field=models.BooleanField(verbose_name=b'Public'),
        ),
        migrations.AlterField(
            model_name='answer',
            name='r',
            field=models.TextField(verbose_name=b'Answer'),
        ),
        migrations.AlterField(
            model_name='answer',
            name='r_date',
            field=models.DateTimeField(verbose_name=b'Date add answer'),
        ),
        migrations.AlterField(
            model_name='question',
            name='q',
            field=models.TextField(verbose_name=b'Question'),
        ),
        migrations.AlterField(
            model_name='question',
            name='q_date',
            field=models.DateTimeField(verbose_name=b'Date insert'),
        ),
    ]
