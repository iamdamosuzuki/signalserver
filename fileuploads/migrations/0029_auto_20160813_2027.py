# -*- coding: utf-8 -*-
# Generated by Django 1.10.dev20160107235441 on 2016-08-13 20:27
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fileuploads', '0028_row_frame_number'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='member',
            unique_together=set([('group', 'file_id')]),
        ),
    ]
