from django.urls import path
from . import views 

urlpatterns = [
    path('', views.index, name='cover'),
    path('house/<str:name>/', views.house, name='house'),
    path('character/<str:name>/', views.character, name='character')
]