# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-01-04 00:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jsonapi', '0023_auto_20170104_0117'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='mash_out_temp',
            field=models.IntegerField(default=75, verbose_name='mash out temperature'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='mash_out_time',
            field=models.IntegerField(default=20, verbose_name='mash out time'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='mashing_temp',
            field=models.IntegerField(default=65, verbose_name='mashing temperature'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='mashing_time',
            field=models.IntegerField(default=60, verbose_name='mashing time'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='primary_fermentation_temp',
            field=models.IntegerField(default=18, verbose_name='primary fermentation temp (C)'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='primary_fermentation_time',
            field=models.IntegerField(default=14, verbose_name='primary fermentation time (days)'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='water_to_malt_ratio',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=4, verbose_name='water to malt ratio'),
        ),
    ]