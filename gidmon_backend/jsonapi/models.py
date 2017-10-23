from django.db import models
from django.contrib.auth.models import User
from decimal import *

class BrewingSystem(models.Model):
	name = models.CharField(max_length=100)
	description = models.TextField(blank=True, null=True)
	boil_off_rate = models.DecimalField(u"evaporation rate in l/hour", max_digits=4, decimal_places=1, default=0)
	transfer_loss = models.DecimalField(u"loss due to transfer to boiler", max_digits=4, decimal_places=1, default=0)
	boiler_dead_space = models.DecimalField(u"dead space when transfering to fermentor", max_digits=4, decimal_places=1, default=0)
	conversion_efficiency = models.IntegerField(u"conversion efficiency (%)", default=100)
	lauter_efficiency = models.IntegerField(u"lautering efficiency (%)", default=100)

	def __str__(self):
		return self.name

# Needed to serialize relations properly
	class JSONAPIMeta:
		resource_name = "brewing_systems"

class BoilIngredient(models.Model):
	name = models.CharField(max_length=100)
	description = models.TextField(blank=True, null=True)
	alpha = models.DecimalField(max_digits=6, decimal_places=2, default=0)
	extract = models.IntegerField(u"sugar content in %", default=0)
	INGREDIENT_TYPES = (
		(u'cones', u'Hops Cones'),
		(u'pellets', u'Hops Pellets'),
		(u'other', u'Other'),
	)
	ingredient_type = models.CharField(max_length=10, choices=INGREDIENT_TYPES, default='cones')

	def __str__(self):
		return u'%s, %f.2%%' % (self.name, self.alpha)

class MashIngredientType(models.Model):
	name = models.CharField(max_length=100)
	description = models.TextField(blank=True, null=True)
	extract_potential = models.IntegerField(default=0)
	is_malt = models.BooleanField(default=True)

	def __str__(self):
		return self.name

class MashIngredient(models.Model):
	name = models.CharField(max_length=100)
	description = models.TextField(blank=True, null=True)
	ebc = models.DecimalField(max_digits=6, decimal_places=2, default=0)
	dbfg = models.DecimalField(max_digits=5, decimal_places=2, default=0)
	mc = models.DecimalField(max_digits=5, decimal_places=2, default=0)
	protein = models.DecimalField(max_digits=5, decimal_places=2, default=0)
	ingredient_type = models.ForeignKey(MashIngredientType)

	def __str__(self):
		return self.name

	# Needed to serialize relations properly
	class JSONAPIMeta:
		resource_name = "mash_ingredients"

class Yeast(models.Model):
	name = models.CharField(max_length=100)
	description = models.TextField(blank=True, null=True)
	fermentation_temp_min = models.IntegerField(default=0)
	fermentation_temp_max = models.IntegerField(default=0)
	ideal_temp_min = models.IntegerField(default=0)
	ideal_temp_max = models.IntegerField(default=0)
	alcohol_tolerance = models.IntegerField(default=0)
	YEAST_TYPES = (
		(u'dry', u'Dry'),
		(u'liquid', u'Liquid'),
	)
	yeast_type = models.CharField(max_length=10, choices=YEAST_TYPES, default='dry')
	attenuation = models.DecimalField(u"attenuation in %", max_digits=3, decimal_places=1, default=0)
	cell_concentration = models.DecimalField(u"billion cells/g", max_digits=5, decimal_places=3, default=0)
	FLOCCULATION_TYPES = (
		(u'low', u'Low'),
		(u'medium', u'Medium'),
		(u'high', u'High'),
	)
	flocculation = models.CharField(max_length=10, choices=FLOCCULATION_TYPES, default='medium')
	
	def __str__(self):
		return self.name

	# Needed to serialize relations properly
	class JSONAPIMeta:
		resource_name = "yeasts"

class BeerType(models.Model):
	name = models.CharField(max_length=100)
	description = models.TextField(blank=True, null=True)
	priming_co2_min = models.DecimalField(u"min CO2 for priming in g/l", max_digits=3, decimal_places=1, default=0)
	priming_co2_max = models.DecimalField(u"max CO2 for priming in g/l", max_digits=3, decimal_places=1, default=0)
	
	def __str__(self):
		return self.name

class Beer(models.Model):
	name = models.CharField(max_length=100)
	description = models.TextField(blank=True, null=True)
	image_name = models.CharField(max_length=30, default='dummy.gif')
	beer_type = models.ForeignKey(BeerType, related_name='beers_of_type')

	def __str__(self):
		return self.name

	# Needed to serialize relations properly
	class JSONAPIMeta:
		resource_name = "beers"

class PitchType(models.Model):
	name = models.CharField(max_length=100)
	pitch_rate = models.DecimalField(u"billion cells/l wort/plato", max_digits=6, decimal_places=2, default=1.0)

	def __str__(self):
		return self.name

	# Needed to serialize relations properly
	class JSONAPIMeta:
		resource_name = "pitch_types"

class Recipe(models.Model):
	beer = models.OneToOneField(Beer, related_name='recipe')
	creator = models.ForeignKey(User)
	mashing_temp = models.IntegerField(u"mashing temperature", default=65)
	mashing_time = models.IntegerField(u"mashing time", default=60)
	mash_out_temp = models.IntegerField(u"mash out temperature", default=75)
	mash_out_time = models.IntegerField(u"mash out time", default=20)
	sparge_count = models.IntegerField(u"number of sparges", default=1)
	sparge_water_temp = models.IntegerField(u"sparge water temperature", default=73)
	sparge_time = models.IntegerField(u"sparge time", default=20)
	pre_boil_volume = models.DecimalField(u"pre boil volume", max_digits=4, decimal_places=2, default=20)
	post_boil_volume = models.DecimalField(u"post boil volume", max_digits=4, decimal_places=2, default=15)
	fermentation_volume = models.DecimalField(u"fermentation volume", max_digits=4, decimal_places=2, default=12)
	boil_time = models.IntegerField(u"time to boil in minutes", default=60)
	total_malt_weight = models.DecimalField(u"total malt weight", max_digits=4, decimal_places=1, default=5)
	primary_fermentation_temp = models.IntegerField(u"primary fermentation temp (C)", default=18)
	primary_fermentation_time = models.IntegerField(u"primary fermentation time (days)", default=14)
	yeast = models.ForeignKey(Yeast, null=True, blank=True)
	yeast_amount = models.DecimalField(u"amount of yeast (g)", max_digits=4, decimal_places=1, default=0)
	pitch_type = models.ForeignKey(PitchType, null=True, blank=True)

	def __str__(self):
		return 'Recipe: %s' % self.beer.name

	# Needed to serialize relations properly
	class JSONAPIMeta:
		resource_name = "recipes"

class BrewingSession(models.Model):
	date = models.DateTimeField();
	recipe = models.ForeignKey(Recipe, related_name='sessions')
	brewing_system = models.ForeignKey(BrewingSystem, null=True)
	strike_water_temp = models.IntegerField(u"measured strike water temperature", default=0)
	sparge_water_temp = models.IntegerField(u"measured sparge water temperature", default=0)
	pre_boil_volume = models.DecimalField(u"measured pre boil volume", max_digits=4, decimal_places=2, default=0)
	post_boil_volume = models.DecimalField(u"measured post boil volume", max_digits=4, decimal_places=2, default=0)
	fermentation_volume = models.DecimalField(u"volume in fermentation vessel", max_digits=4, decimal_places=2, default=0)
	measured_first_wort_sg = models.DecimalField(u"measured first wort sg", max_digits=4, decimal_places=3, default=1.000)
	measured_first_sparge_sg = models.DecimalField(u"measured first sparge sg", max_digits=4, decimal_places=3, default=1.000)
	measured_pre_boil_sg = models.DecimalField(u"measured pre boil sg", max_digits=4, decimal_places=3, default=1.000)
	measured_og = models.DecimalField(u"measured og", max_digits=4, decimal_places=3, default=1.000)
	measured_fg = models.DecimalField(u"measured fg", max_digits=4, decimal_places=3, default=1.000)
	wort_settle_time = models.IntegerField(u"time to let the sediment settle in the wort", default=0)
	yeast_used = models.DecimalField(u"amount of yeast used", max_digits=4, decimal_places=2, default=0)

	def __str__(self):
		return 'Session: %s %s' % (self.recipe.beer.name, self.date)

	# Needed to serialize relations properly
	class JSONAPIMeta:
		resource_name = "brewing_sessions"

class BrewingSessionComment(models.Model):
	brewing_session = models.ForeignKey(BrewingSession, related_name='comments')
	parent = models.ForeignKey('self', related_name='children', null=True, blank=True) 
	content = models.TextField()
	author = models.ForeignKey(User)

	def __str__(self):
		return 'Comment on: %s %s' % (self.brewing_session.recipe.beer.name, self.brewing_session.date)

	# Needed to serialize relations properly
	class JSONAPIMeta:
		resource_name = "brewing_session_comments"

class BeerBatch(models.Model):
	name = models.CharField(max_length=100)
	abv = models.IntegerField(default=0)
	untappd_url = models.CharField(max_length=100)
	session = models.OneToOneField(BrewingSession, related_name='beer_batch');

	def __str__(self):
		return u'Beer Batch: %s' % (self.name)

class BoilRecipeEntry(models.Model):
	recipe = models.ForeignKey(Recipe, related_name='boil_entries')
	ingredient = models.ForeignKey(BoilIngredient)
	amount = models.IntegerField(u'amount in grams', default=0)
	boil_time = models.IntegerField(u'time to boil in mins', default=0)

	def __str__(self):
		return u'Recipe Entry: %s, %s, %s min' % (self.recipe.beer.name, self.ingredient.name, self.boil_time)

	# Needed to serialize relations properly
	class JSONAPIMeta:
		resource_name = "boil_recipe_entries"

class MashRecipeEntry(models.Model):
	recipe = models.ForeignKey(Recipe, related_name='mash_entries')
	ingredient = models.ForeignKey(MashIngredient)
	amount = models.DecimalField(u'amount of malt in %', max_digits=4, decimal_places=1, default=0)
	
	def __str__(self):
		return u'Recipe Entry: %s, %s' % (self.recipe.beer.name, self.ingredient.name)

	# Needed to serialize relations properly
	class JSONAPIMeta:
		resource_name = "mash_recipe_entries"

class BoilSessionEntry(models.Model):
	session = models.ForeignKey(BrewingSession, related_name='boil_entries')
	recipe_entry = models.ForeignKey(BoilRecipeEntry)
	alpha = models.DecimalField(max_digits=6, decimal_places=2, default=0)

	def __str__(self):
		return u'Session Entry: %s, %s, %s min' % (self.session.recipe.beer.name, self.recipe_entry.ingredient.name, self.recipe_entry.boil_time)

	# Needed to serialize relations properly
	class JSONAPIMeta:
		resource_name = "boil_session_entries"

class NewsItem(models.Model):
	title = models.CharField(max_length=100)
	preamble = models.TextField()
	content = models.TextField()
	created = models.DateTimeField()
	author = models.ForeignKey(User)

	def __str__(self):
		return self.title

	# Needed to serialize relations properly
	class JSONAPIMeta:
		resource_name = "news_items"
		
class NewsComment(models.Model):
	news_item = models.ForeignKey(NewsItem, related_name='comments')
	parent = models.ForeignKey('self', related_name='children', null=True, blank=True) 
	content = models.TextField()
	author = models.ForeignKey(User)

	def __str__(self):
		return 'Comment on: %s' % self.news_item.title

	# Needed to serialize relations properly
	class JSONAPIMeta:
		resource_name = "news_comments"

class Profile(models.Model):
	user = models.OneToOneField(User, related_name='profile')
	picture = models.ImageField(upload_to='profile_picture')

	def __str__(self):
		return 'Profile for: %s' % self.user.username