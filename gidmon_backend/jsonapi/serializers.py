from django.contrib.auth.models import User, Group
from rest_framework_json_api import serializers
#from rest_framework_json_api import serializers
from gidmon_backend.jsonapi import models

class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		resource_name = "user"
		fields = ('url', 'username', 'first_name', 'last_name', 'email', 'groups', 'is_staff', 'is_superuser', 'profile')
		read_only_fields = ('profile',)

class GroupSerializer(serializers.ModelSerializer):
	class Meta:
		model = Group
		resource_name = "group"
		fields = ('url', 'name')

class ProfileSerializer(serializers.ModelSerializer):
	class Meta:
		model = models.Profile
		resource_name = "profiles"
		fields = '__all__'
		read_only_fields = ('user', 'picture')

class BrewingSystemSerializer(serializers.ModelSerializer):
	class Meta:
		model = models.BrewingSystem
		resource_name = "brewing_systems"
		fields = '__all__'

class HopsSerializer(serializers.ModelSerializer):
	class Meta:
		model = models.Hops
		resource_name = "hops"
		fields = '__all__'

class MaltTypeSerializer(serializers.ModelSerializer):
	class Meta:
		model = models.MaltType
		resource_name = "malt_types"
		fields = '__all__'

class MaltSerializer(serializers.ModelSerializer):
	class Meta:
		model = models.Malt
		resource_name = "malts"
		fields = '__all__'

class YeastSerializer(serializers.ModelSerializer):
	class Meta:
		model = models.Yeast
		resource_name = "yeasts"
		fields = '__all__'

class MiscIngredientSerializer(serializers.ModelSerializer):
	class Meta:
		model = models.MiscIngredient
		resource_name = "misc_ingredients"
		fields = '__all__'

class BeerTypeSerializer(serializers.ModelSerializer):
	class Meta:
		model = models.BeerType
		resource_name = "beer_types"
		fields = '__all__'

class BeerSerializer(serializers.ModelSerializer):
	class Meta:
		model = models.Beer
		resource_name = "beers"
		fields = '__all__'

class RecipeSerializer(serializers.ModelSerializer):
	included_serializers = {
		'yeast': YeastSerializer,
	}
	class Meta:
		model = models.Recipe
		resource_name = "recipes"
		fields = ('beer', 'creator', 'mashing_temp', 'mashing_time', 'mash_out_temp', 'mash_out_time', 'sparge_count', 'sparge_water_temp', 
			'pre_boil_volume', 'primary_fermentation_temp', 'primary_fermentation_time', 'yeast', 'yeast_amount', 'target_pitch_rate',
			'hops_entries', 'malt_entries', 'misc_entries')
		read_only_fields = ('beer', 'creator', 'hops_entries', 'malt_entries', 'misc_entries')

class BrewingSessionSerializer(serializers.ModelSerializer):
	class Meta:
		model = models.BrewingSession
		resource_name = "brewing_sessions"
		fields = '__all__'

class BeerBatchSerializer(serializers.ModelSerializer):
	class Meta:
		model = models.BeerBatch
		resource_name = "beer_batches"
		fields = '__all__'

class HopeRecipeEntrySerializer(serializers.ModelSerializer):
	class Meta:
		model = models.HopsRecipeEntry
		resource_name = "hops_recipe_entries"
		fields = '__all__'

class MaltRecipeEntrySerializer(serializers.ModelSerializer):
	class Meta:
		model = models.MaltRecipeEntry
		resource_name = "malt_recipe_entries"
		fields = '__all__'

class MiscIngredientEntrySerializer(serializers.ModelSerializer):
	class Meta:
		model = models.MiscIngredientEntry
		resource_name = "misc_ingredient_entries"
		fields = '__all__'
		
class NewsCommentSerializer(serializers.ModelSerializer):
	included_serializers = {
		'author': UserSerializer,
	}
	class Meta:
		model = models.NewsComment
		resource_name = "news_comments"
		fields = ('content', 'children', 'author', 'news_item')
		read_only_fields = ('children', 'author')
		
class NewsItemSerializer(serializers.ModelSerializer):
	included_serializers = {
		'author': UserSerializer,
		'comments': NewsCommentSerializer
	}
	class Meta:
		model = models.NewsItem
		resource_name = "news_items"
		fields = ('title', 'preamble', 'content', 'created', 'author', 'comments')
		read_only_fields = ('author', 'comments')
