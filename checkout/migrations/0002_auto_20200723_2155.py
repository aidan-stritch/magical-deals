# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-07-23 21:55
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orderlineitem',
            old_name='oder',
            new_name='order',
        ),
    ]
