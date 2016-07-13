from django.contrib.auth.models import User, Group
from rest_framework import serializers
#from rest_framework_json_api import serializers
from gidmon_backend.jsonapi.models import Beer


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        resource_name = "user"
        fields = ('url', 'username', 'email', 'groups')

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        resource_name = "group"
        fields = ('url', 'name')

class BeerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Beer
        resource_name = "beers"
        fields = '__all__'
