# -*- coding: utf-8 -*-
# Generated by Django 1.11.26 on 2020-02-19 16:18
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='AccountDetails',
            new_name='AccountDetail',
        ),
        migrations.RenameModel(
            old_name='UserAddress',
            new_name='UserAddresse',
        ),
    ]
