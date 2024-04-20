# Create your models here.

from django.db import models
from django.contrib.auth.models import User

class Libro(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=200)
    editorial = models.CharField(max_length=100)
    fecha_publicacion = models.DateField()
    idioma = models.CharField(max_length=50)

    def __str__(self):
        return self.titulo

class Avatar(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='avatares/', null=True, blank=True)

    def __str__(self):
        return f"Avatar de {self.user.username}"