# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2019-07-18 20:11
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('communities', '0003_auto_20160819_1913'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='communitymember',
            options={'permissions': (('ban_member', 'Can ban members'),)},
        ),
    ]
