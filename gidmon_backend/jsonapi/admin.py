from django.contrib import admin
from gidmon_backend.jsonapi.models import Beer, Recipe

# Register your models here.
admin.site.register(Beer)
admin.site.register(Recipe)
