# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-15 01:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zc_demo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='zingchartconfig',
            name='idleRangeHigh',
            field=models.IntegerField(default=28),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='zingchartconfig',
            name='idleRangeLow',
            field=models.IntegerField(default=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='zingchartconfig',
            name='warningRangeHigh',
            field=models.IntegerField(default=29),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='zingchartconfig',
            name='warningRangeLow',
            field=models.IntegerField(default=38),
            preserve_default=False,
        ),
    ]
