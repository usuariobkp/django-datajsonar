# -*- coding: utf-8 -*-
# Generated by Django 1.11.23 on 2019-08-27 19:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_datajsonar', '0012_auto_20190610_1209'),
    ]

    operations = [
        migrations.AddField(
            model_name='dataset',
            name='starred',
            field=models.BooleanField(default=False),
        )
    ]
