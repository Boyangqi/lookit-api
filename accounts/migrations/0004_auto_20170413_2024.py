# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-13 20:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20170413_1659'),
    ]

    operations = [
        migrations.AddField(
            model_name='participantprofile',
            name='annual_income',
            field=models.TextField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='participantprofile',
            name='languages_spoken_at_home',
            field=models.TextField(verbose_name='languages spoken at home'),
        ),
    ]