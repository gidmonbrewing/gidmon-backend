from django.db import models

class Beer(models.Model):
    name = models.CharField(max_length=100)
    abv = models.IntegerField(default=0)

    class JSONAPIMeta:
        resource_name = "beers"
