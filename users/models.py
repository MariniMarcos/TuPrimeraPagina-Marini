from django.db import models

from django.contrib.auth.models import User

class imagen(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='imagenes/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Imagen de {self.usuario}'