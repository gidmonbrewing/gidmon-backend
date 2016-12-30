from django.contrib import admin
from gidmon_backend.jsonapi import models

# Register your models here.
admin.site.register(models.BrewingSystem)
admin.site.register(models.Hops)
admin.site.register(models.MaltType)
admin.site.register(models.Malt)
admin.site.register(models.Yeast)
admin.site.register(models.MiscIngredient)
admin.site.register(models.BeerType)
admin.site.register(models.Beer)
admin.site.register(models.Recipe)
admin.site.register(models.NewsItem)
admin.site.register(models.NewsComment)
admin.site.register(models.Profile)
