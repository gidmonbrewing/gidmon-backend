from django.db import models

class Beer(models.Model):
    name = models.CharField(max_length=100)
    abv = models.IntegerField(default=0)

    def __str__(self):
        return self.name

    class JSONAPIMeta:
        resource_name = "beers"

class Recipe(models.Model):
    beer = models.OneToOneField(Beer)

    def __str__(self):
        return 'Recipe: %s' % self.beer.name
