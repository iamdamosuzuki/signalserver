# -*- coding: utf-8 -*-
# Generated by Django 1.10.dev20160107235441 on 2016-11-02 20:06
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('policies', '0003_auto_20161024_2342'),
    ]

    operations = [
        migrations.AddField(
            model_name='policy',
            name='last_updated_time',
            field=models.DateTimeField(auto_now=True, default=datetime.datetime(2016, 11, 2, 20, 6, 5, 645468, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='policy',
            name='user_name',
            field=models.CharField(default=None, max_length=400, null=True),
        ),
    ]