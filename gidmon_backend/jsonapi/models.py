from django.db import models
from django.contrib.auth.models import User

class Beer(models.Model):
	name = models.CharField(max_length=100)
	description = models.TextField()
	abv = models.IntegerField(default=0)
	image_name = models.CharField(max_length=30)
	untappd_url = models.CharField(max_length=100)

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

	class JSONAPIMeta:
		resource_name = "news_items"
		
class NewsComment(models.Model):
	news_item = models.ForeignKey(NewsItem, related_name='comments')
	parent = models.ForeignKey('self', related_name='children', null=True, blank=True) 
	content = models.TextField()
	author = models.ForeignKey(User)

	def __str__(self):
		return 'Comment on: %s' % self.news_item.title

	class JSONAPIMeta:
		resource_name = "news_comments"

class Profile(models.Model):
	user = models.ForeignKey(User)
	picture = models.ImageField(upload_to='profile_picture')

	def __str__(self):
		return 'Profile for: %s' % self.user.username