# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-12-20 23:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='set',
            name='border_colour',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
