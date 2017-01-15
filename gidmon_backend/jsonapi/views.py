from django.shortcuts import render
from django.contrib.auth.models import User, Group
from rest_framework import viewsets, views
from rest_framework.response import Response
from gidmon_backend.jsonapi import serializers
from gidmon_backend.jsonapi import models
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import status
from rest_framework.settings import api_settings
from rest_framework.decorators import detail_route
import os
import time


class UserViewSet(viewsets.ModelViewSet):
	"""
	API endpoint that allows users to be viewed or edited.
	"""
	queryset = User.objects.all().order_by('-date_joined')
	serializer_class = serializers.UserSerializer

class GroupViewSet(viewsets.ModelViewSet):
	"""
	API endpoint that allows groups to be viewed or edited.
	"""
	queryset = Group.objects.all()
	serializer_class = serializers.GroupSerializer

class ProfileViewSet(viewsets.ModelViewSet):
	queryset = models.Profile.objects.all()
	serializer_class = serializers.ProfileSerializer

	@detail_route(methods=['post'])
	def set_picture(self, request, pk=None):
		if 'file' in request.data:
			upload = request.data['file']

			# request.user will be set to the current user by TokenAuthenticator
			profile = self.get_object()

			# Only admins can change other users picture
			if profile.user != request.user:
				if not request.user.is_staff:
					return Response({ "detail": "Only admins can change other users profile picture" }, status=status.HTTP_403_FORBIDDEN);

			# We do not want to call delete if no picture is set.
			# ImageField(picture) will return false when it's not set.
			if profile.picture:
				profile.picture.delete()

			# We extract the extension of the uploaded picture and use it together with the username
			filename, file_extension = os.path.splitext(upload.name)
			picture_name = '%s_%i%s' % (profile.user.username, int(time.time()), file_extension)
			profile.picture.save(picture_name, upload)
			serializer = self.get_serializer(profile)
			headers = self.get_success_headers(serializer.data)
			return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
		else:
			return Response(status=status.HTTP_400_BAD_REQUEST)

class BrewingSystemViewSet(viewsets.ModelViewSet):
	queryset = models.BrewingSystem.objects.all();
	serializer_class = serializers.BrewingSystemSerializer

class MashIngredientViewSet(viewsets.ModelViewSet):
	queryset = models.MashIngredient.objects.all()
	serializer_class = serializers.MashIngredientSerializer

class BoilIngredientViewSet(viewsets.ModelViewSet):
	queryset = models.BoilIngredient.objects.all()
	serializer_class = serializers.BoilIngredientSerializer

class YeastViewSet(viewsets.ModelViewSet):
	queryset = models.Yeast.objects.all()
	serializer_class = serializers.YeastSerializer

class BeerViewSet(viewsets.ModelViewSet):
	queryset = models.Beer.objects.all()
	serializer_class = serializers.BeerSerializer

class RecipeViewSet(viewsets.ModelViewSet):
	queryset = models.Recipe.objects.all()
	serializer_class = serializers.RecipeSerializer

#    def create(self, request):
#        print(request.data);

class BrewingSessionViewSet(viewsets.ModelViewSet):
	queryset = models.BrewingSession.objects.all()
	serializer_class = serializers.BrewingSessionSerializer

class MashRecipeEntryViewSet(viewsets.ModelViewSet):
	queryset = models.MashRecipeEntry.objects.all()
	serializer_class = serializers.MashRecipeEntrySerializer

class BoilRecipeEntryViewSet(viewsets.ModelViewSet):
	queryset = models.BoilRecipeEntry.objects.all()
	serializer_class = serializers.BoilRecipeEntrySerializer

class NewsItemViewSet(viewsets.ModelViewSet):
	queryset = models.NewsItem.objects.all()
	serializer_class = serializers.NewsItemSerializer

	def perform_create(self, serializer):
		serializer.save(author=self.request.user)
	
class NewsCommentViewSet(viewsets.ModelViewSet):
	queryset = models.NewsComment.objects.all()
	serializer_class = serializers.NewsCommentSerializer

	def perform_create(self, serializer):
		serializer.save(author=self.request.user)
