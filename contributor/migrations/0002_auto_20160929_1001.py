# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-29 17:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contributor', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contributionsync',
            name='pre_state_behind_main',
            field=models.NullBooleanField(),
        ),
        migrations.AlterField(
            model_name='contributionsync',
            name='pre_state_uncommitted_changes',
            field=models.NullBooleanField(),
        ),
        migrations.AlterField(
            model_name='contributionsync',
            name='pre_state_undeployed_commit',
            field=models.NullBooleanField(),
        ),
    ]
