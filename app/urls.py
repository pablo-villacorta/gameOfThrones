from django.urls import path
from . import views 

urlpatterns = [
    path('lore/', views.index, name='cover'),
    path('lore/house/<str:name>/', views.house, name='house'),
    path('lore/character/<str:name>/', views.character, name='character'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('forum/', views.ThreadListView.as_view(), name='threads'),
    path('forum/thread/<int:id>', views.PostListView.as_view(), name='thread'),
    path('forum/thread/<int:id>/new', views.newPost, name='new_post'),
    path('forum/newthread/', views.newThread, name='new_thread')
]