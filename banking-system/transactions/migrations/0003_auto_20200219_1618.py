# -*- coding: utf-8 -*-
# Generated by Django 1.11.26 on 2020-02-19 16:18
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0002_auto_20190504_2012'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Diposit',
            new_name='Deposit',
        ),
    ]
