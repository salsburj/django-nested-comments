# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-10-31 17:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0003_auto_20170104_1329'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commentversion',
            name='message',
            field=models.TextField(blank=True),
        ),
    ]
