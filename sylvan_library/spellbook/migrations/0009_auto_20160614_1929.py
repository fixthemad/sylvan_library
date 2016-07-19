# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-14 09:29
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('spellbook', '0008_block_start_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='block',
            name='start_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]