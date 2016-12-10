from django.db import models
from django.contrib.auth.models import User

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
		
class NewsItem(models.Model):
	title = models.CharField(max_length=100)
	preamble = models.TextField()
	content = models.TextField()
	created = models.DateTimeField()
	author = models.ForeignKey(User)

	def __str__(self):
		return self.title
		
class NewsComment(models.Model):
	news_item = models.ForeignKey(NewsItem, related_name='comments')
	content = models.TextField()

	def __str__(self):
		return 'Comment on: %s' % self.news_item.title