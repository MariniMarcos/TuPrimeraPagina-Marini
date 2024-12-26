from django.urls import path, include
from . import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('', views.index, name='index'),
    path('create_post/', views.create_post, name='create_post'),
    path('list_posts/', views.list_posts, name='list_posts'),
    path('search_posts/', views.search_posts, name='search_posts'),
    path('about/', views.about, name='about'),
    path('users/', include('users.urls')),
    path('edit_post/<int:pk>/', views.edit_post, name='edit_post'),
    path('detail_posts/<int:post_id>/', views.detail_posts, name='detail_posts'),
    path('delete_post/<int:pk>/', views.delete_post, name='delete_post'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
