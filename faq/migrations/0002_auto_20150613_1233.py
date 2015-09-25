# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('faq', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='answer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('r', models.TextField()),
                ('r_date', models.DateTimeField(verbose_name=b'data request')),
                ('public', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='question',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('q', models.TextField()),
                ('q_date', models.DateTimeField(verbose_name=b'data quote')),
            ],
        ),
        migrations.DeleteModel(
            name='quote',
        ),
        migrations.AddField(
            model_name='answer',
            name='child',
            field=models.ForeignKey(to='faq.question'),
        ),
    ]
