# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-08-16 20:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20200816_1952'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usercreate',
            name='add_Line_One',
            field=models.CharField(default='', help_text='e.g. Apt Number', max_length=254),
        ),
        migrations.AlterField(
            model_name='usercreate',
            name='add_Line_Two',
            field=models.CharField(default='', help_text='e.g. Street', max_length=254),
        ),
        migrations.AlterField(
            model_name='usercreate',
            name='phone',
            field=models.CharField(default='', help_text='e.g. +353 (0) 555 2258', max_length=254),
        ),
        migrations.AlterField(
            model_name='usercreate',
            name='staff',
            field=models.BooleanField(default=False, help_text='Please indicate whether this user is staff or not'),
        ),
    ]
