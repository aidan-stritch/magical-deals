# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-08-16 20:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_auto_20200816_2035'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usercreate',
            name='profile_Image',
            field=models.FileField(help_text='Please use a clear image', upload_to='profile'),
        ),
    ]
