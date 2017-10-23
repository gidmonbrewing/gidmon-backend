# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-01-18 20:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jsonapi', '0029_auto_20170118_2101'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='fermentation_volume',
            field=models.DecimalField(decimal_places=2, default=12, max_digits=4, verbose_name='fermentation volume'),
        ),
    ]