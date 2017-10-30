# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-10-30 21:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jsonapi', '0044_auto_20171030_2127'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mashsessionentry',
            name='amount',
        ),
        migrations.AddField(
            model_name='mashsessionentry',
            name='weight',
            field=models.DecimalField(decimal_places=1, default=0, max_digits=4, verbose_name='amount of malt in kg'),
        ),
    ]
