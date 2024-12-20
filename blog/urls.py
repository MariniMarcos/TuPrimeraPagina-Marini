from django.urls import path, include
from . import views
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('', views.index, name='index'),
    path('create_post/', views.create_post, name='create_post'),
    path('list_posts/', views.list_posts, name='list_posts'),
    path('search_posts/', views.search_posts, name='search_posts'),
    path('about/', views.about, name='about'),
    path('users/', include('users.urls')),
]