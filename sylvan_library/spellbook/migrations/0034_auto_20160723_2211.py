# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-23 12:11
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('spellbook', '0033_auto_20160723_2209'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userownedcard',
            name='card_printing_language',
        ),
        migrations.AlterField(
            model_name='usercardchange',
            name='physical_card',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='spellbook.PhysicalCard'),
        ),
        migrations.AlterField(
            model_name='userownedcard',
            name='physical_card',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='spellbook.PhysicalCard'),
        ),
    ]