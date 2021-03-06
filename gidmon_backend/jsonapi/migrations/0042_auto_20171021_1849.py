# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-10-21 16:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jsonapi', '0041_brewingsessioncomment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='pitch_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='jsonapi.PitchType'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='yeast',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='jsonapi.Yeast'),
        ),
    ]
