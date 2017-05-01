# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-11-06 00:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spellbook', '0048_auto_20161106_1106'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='cardlink',
            unique_together=set([]),
        ),
        migrations.RemoveField(
            model_name='cardlink',
            name='card_from',
        ),
        migrations.RemoveField(
            model_name='cardlink',
            name='card_to',
        ),
        migrations.AddField(
            model_name='card',
            name='links',
            field=models.ManyToManyField(related_name='_card_links_+', to='spellbook.Card'),
        ),
        migrations.DeleteModel(
            name='CardLink',
        ),
    ]