# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-10-30 20:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jsonapi', '0043_recipe_sparge_time'),
    ]

    operations = [
        migrations.CreateModel(
            name='MashSessionEntry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=1, default=0, max_digits=4, verbose_name='amount of malt in %')),
                ('recipe_entry', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jsonapi.MashRecipeEntry')),
            ],
        ),
        migrations.AddField(
            model_name='brewingsession',
            name='measured_fermentation_volume',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=4, verbose_name='measured volume in fermentation vessel'),
        ),
        migrations.AddField(
            model_name='brewingsession',
            name='measured_post_boil_volume',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=4, verbose_name='measured post boil volume'),
        ),
        migrations.AddField(
            model_name='brewingsession',
            name='measured_pre_boil_volume',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=4, verbose_name='measured pre boil volume'),
        ),
        migrations.AddField(
            model_name='brewingsession',
            name='sparge_water_volume',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=4, verbose_name='scale adjusted sparge water volume'),
        ),
        migrations.AddField(
            model_name='brewingsession',
            name='strike_water_volume',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=4, verbose_name='scale adjusted strike water volume'),
        ),
        migrations.AddField(
            model_name='recipe',
            name='conversion_efficiency',
            field=models.IntegerField(default=95, verbose_name='the assumed conversion efficiency of brewing equipment'),
        ),
        migrations.AlterField(
            model_name='brewingsession',
            name='fermentation_volume',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=4, verbose_name='scale adjusted volume in fermentation vessel'),
        ),
        migrations.AlterField(
            model_name='brewingsession',
            name='post_boil_volume',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=4, verbose_name='scale adjusted post boil volume'),
        ),
        migrations.AlterField(
            model_name='brewingsession',
            name='pre_boil_volume',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=4, verbose_name='scale adjusted pre boil volume'),
        ),
        migrations.AddField(
            model_name='mashsessionentry',
            name='session',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mash_entries', to='jsonapi.BrewingSession'),
        ),
    ]