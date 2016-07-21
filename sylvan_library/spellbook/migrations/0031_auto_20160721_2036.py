# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-21 10:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('spellbook', '0030_auto_20160716_1751'),
    ]

    operations = [
        migrations.AddField(
            model_name='card',
            name='name',
            field=models.CharField(default='DEFAULT_CARD_NAME', max_length=200),
        ),
        migrations.AlterField(
            model_name='cardlink',
            name='card_from',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cardFrom', to='spellbook.Card'),
        ),
    ]
