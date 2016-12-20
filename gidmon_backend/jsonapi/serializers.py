from django.contrib.auth.models import User, Group
from rest_framework_json_api import serializers
#from rest_framework_json_api import serializers
from gidmon_backend.jsonapi.models import Beer, Recipe, NewsItem, NewsComment, Profile

class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		resource_name = "user"
		fields = ('url', 'username', 'first_name', 'last_name', 'email', 'groups', 'is_staff', 'is_superuser')

class GroupSerializer(serializers.ModelSerializer):
	class Meta:
		model = Group
		resource_name = "group"
		fields = ('url', 'name')

class ProfileSerializer(serializers.ModelSerializer):
	class Meta:
		model = Profile
		resource_name = "profiles"
		fields = '__all__'
		read_only_fields = ('user', 'picture')

class BeerSerializer(serializers.ModelSerializer):
	class Meta:
		model = Beer
		resource_name = "beers"
		fields = '__all__'

class RecipeSerializer(serializers.ModelSerializer):
	class Meta:
		model = Recipe
		resource_name = "recipes"
		fields = '__all__'
		
class NewsCommentSerializer(serializers.ModelSerializer):
	included_serializers = {
		'author': UserSerializer,
	}
	class Meta:
		model = NewsComment
		resource_name = "news_comments"
		fields = ('content', 'children', 'author', 'news_item')
		read_only_fields = ('children', 'author')
		
class NewsItemSerializer(serializers.ModelSerializer):
	included_serializers = {
		'author': UserSerializer,
		'comments': NewsCommentSerializer
	}
	class Meta:
		model = NewsItem
		resource_name = "news_items"
		fields = ('title', 'preamble', 'content', 'created', 'author', 'comments')
		read_only_fields = ('author', 'comments')
