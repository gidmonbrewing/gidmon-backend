from django.contrib import admin
from gidmon_backend.jsonapi.models import BrewingSystem, Hops, BeerType, MaltType, Beer, Recipe, NewsItem, NewsComment, Profile

# Register your models here.
admin.site.register(BrewingSystem)
admin.site.register(Hops)
admin.site.register(BeerType)
admin.site.register(MaltType)
admin.site.register(Beer)
admin.site.register(Recipe)
admin.site.register(NewsItem)
admin.site.register(NewsComment)
admin.site.register(Profile)
