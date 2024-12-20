from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from users.views import users_login, users_registro, users_profile
from . import views

urlpatterns = [
    # Ruta para iniciar sesión
    path('login/', LoginView.as_view(template_name='users/login.html'), name='login'),

    # Ruta para registrarse
    path('register/', users_registro, name='registro'),

    # Ruta para el perfil de usuario
    path('profile/', LoginView.as_view(template_name='users/editar_usuario.html'), name='profile'),

    # Ruta para cerrar sesión
    path('logout/', LogoutView.as_view(next_page='index'), name='logout'),

    # Ruta para la página de inicio
    path('blog/', views.blog_index, name='blog'),
]



