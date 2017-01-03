from django.contrib import admin
from gidmon_backend.jsonapi import models

# Register your models here.
admin.site.register(models.BrewingSystem)
admin.site.register(models.BoilIngredient)
admin.site.register(models.MashIngredientType)
admin.site.register(models.MashIngredient)
admin.site.register(models.Yeast)
admin.site.register(models.BeerType)
admin.site.register(models.Beer)
admin.site.register(models.Recipe)
admin.site.register(models.BrewingSession)
admin.site.register(models.BeerBatch)
admin.site.register(models.BoilRecipeEntry)
admin.site.register(models.MashRecipeEntry)
admin.site.register(models.NewsItem)
admin.site.register(models.NewsComment)
admin.site.register(models.Profile)
