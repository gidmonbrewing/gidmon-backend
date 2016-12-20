from django.shortcuts import render
from django.contrib.auth.models import User, Group
from rest_framework import viewsets, views
from rest_framework.response import Response
from gidmon_backend.jsonapi.serializers import UserSerializer, GroupSerializer, BeerSerializer, RecipeSerializer, NewsItemSerializer, NewsCommentSerializer, ProfileSerializer
from gidmon_backend.jsonapi.models import Beer, Recipe, NewsItem, NewsComment, Profile
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import status
import os


class UserViewSet(viewsets.ModelViewSet):
	"""
	API endpoint that allows users to be viewed or edited.
	"""
	queryset = User.objects.all().order_by('-date_joined')
	serializer_class = UserSerializer

class GroupViewSet(viewsets.ModelViewSet):
	"""
	API endpoint that allows groups to be viewed or edited.
	"""
	queryset = Group.objects.all()
	serializer_class = GroupSerializer

class ProfileViewSet(viewsets.ModelViewSet):
	queryset = Profile.objects.all()
	serializer_class = ProfileSerializer

class ProfilePictureView(views.APIView):
	parser_classes = (MultiPartParser, FormParser)

	def post(self, request, *args, **kwargs):
		if 'file' in request.data:
			upload = request.data['file']
			profile = Profile.objects.get(user=request.user)
			if profile.picture:
				profile.picture.delete()

			filename, file_extension = os.path.splitext(upload.name)
			picture_name = request.user.username + file_extension
			profile.picture.save(picture_name, upload)
			return Response(status=status.HTTP_201_CREATED, headers={'Location': picture_name})
		else:
			return Response(status=status.HTTP_400_BAD_REQUEST)

class BeerViewSet(viewsets.ModelViewSet):
	queryset = Beer.objects.all()
	serializer_class = BeerSerializer

class RecipeViewSet(viewsets.ModelViewSet):
	queryset = Recipe.objects.all()
	serializer_class = RecipeSerializer

#    def create(self, request):
#        print(request.data);

class NewsItemViewSet(viewsets.ModelViewSet):
	queryset = NewsItem.objects.all()
	serializer_class = NewsItemSerializer

	def perform_create(self, serializer):
		serializer.save(author=self.request.user)
	
class NewsCommentViewSet(viewsets.ModelViewSet):
	queryset = NewsComment.objects.all()
	serializer_class = NewsCommentSerializer

	def perform_create(self, serializer):
		serializer.save(author=self.request.user)
