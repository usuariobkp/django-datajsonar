# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-10-11 12:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_datajsonar', '0013_stage_synchronizer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='baseregisterfile',
            name='created',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='baseregisterfile',
            name='modified',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='readdatajsontask',
            name='created',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]