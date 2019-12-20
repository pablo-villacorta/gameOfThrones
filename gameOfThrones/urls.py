"""gameOfThrones URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url
from app import views, api_views
from django.conf.urls.i18n import i18n_patterns

from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'characters', api_views.CharacterViewSet)
router.register(r'houses', api_views.HouseViewSet)
router.register(r'episodes', api_views.EpisodeViewSet)

handler404 = views.handler404

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/charactersByName', api_views.CharacterNameView.as_view()),
    path('api/housesByName', api_views.HouseNameView.as_view()),
    path('api/episodesByTitle', api_views.EpisodeNameView.as_view()),
    path('api/charactersByID', api_views.CharacterIDView.as_view()),
    path('api/housesByID', api_views.HouseIDView.as_view()),
    #path('', include('app.urls'))
    path('login_/', views.loginPOST),
    path('register_/', views.registerPOST)
]

urlpatterns += i18n_patterns(
    url(r'^', include('app.urls'))
)
