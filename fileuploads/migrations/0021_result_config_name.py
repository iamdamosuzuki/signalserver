# -*- coding: utf-8 -*-
# Generated by Django 1.10.dev20160107235441 on 2016-06-14 01:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fileuploads', '0020_auto_20160613_2256'),
    ]

    operations = [
        migrations.AddField(
            model_name='result',
            name='config_name',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]