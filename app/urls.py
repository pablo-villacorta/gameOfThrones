from django.urls import path
from django.conf.urls import url, include
from . import views 

urlpatterns = [
    path('', views.home, name='home'),
    url(r'^i18n/', include('django.conf.urls.i18n')),
    path('lore/', views.index, name='cover'),
    path('lore/house/<int:id>/', views.house, name='house'),
    path('lore/character/<int:id>/', views.character, name='character'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('forum/', views.ThreadListView.as_view(), name='threads'),
    path('forum/thread/<int:id>', views.PostListView.as_view(), name='thread'),
    path('forum/thread/<int:id>/new', views.newPost, name='new_post'),
    path('forum/newthread/', views.newThread, name='new_thread'),
    path('quiz', views.quiz, name="quiz"),
    path('lore/episode/<int:id>', views.episode, name='episode'),
    path('lore/season/<int:id>', views.season, name='season')
]
