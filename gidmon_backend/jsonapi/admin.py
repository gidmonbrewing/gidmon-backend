from django.contrib import admin
from gidmon_backend.jsonapi.models import Beer, Recipe, NewsItem, NewsComment

# Register your models here.
admin.site.register(Beer)
admin.site.register(Recipe)
admin.site.register(NewsItem)
admin.site.register(NewsComment)
