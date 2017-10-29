"""gidmon_backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import routers
from gidmon_backend.jsonapi import views
from rest_framework.authtoken.views import obtain_auth_token
from django.conf.urls.static import static
from django.conf import settings

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'beers', views.BeerViewSet)
router.register(r'recipes', views.RecipeViewSet)
router.register(r'news_items', views.NewsItemViewSet)
router.register(r'news_comments', views.NewsCommentViewSet)
router.register(r'profiles', views.ProfileViewSet)
router.register(r'mash_recipe_entries', views.MashRecipeEntryViewSet)
router.register(r'mash_ingredients', views.MashIngredientViewSet)
router.register(r'yeasts', views.YeastViewSet)
router.register(r'boil_ingredients', views.BoilIngredientViewSet)
router.register(r'boil_recipe_entries', views.BoilRecipeEntryViewSet)
router.register(r'brewing_sessions', views.BrewingSessionViewSet)
router.register(r'brewing_session_comments', views.BrewingSessionCommentViewSet)
router.register(r'brewing_systems', views.BrewingSystemViewSet)
router.register(r'pitch_types', views.PitchTypeViewSet)
router.register(r'beer_types', views.BeerTypeViewSet)
router.register(r'boil_session_entries', views.BoilSessionEntryViewSet)

urlpatterns = [
	url(r'^api/token-auth', obtain_auth_token),
	url(r'^api/oauth-login-fb', views.oauth_login_fb),
	url(r'^api/', include(router.urls)),
	url(r'^admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
