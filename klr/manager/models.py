#encoding:utf-8
from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin

class Respuesta(models.Model):
    texto = models.CharField(max_length=500)
    usuario = models.ForeignKey(User)

class Comentario(models.Model):
    texto = models.CharField(max_length=500)
    usuario = models.ForeignKey(User)

class Foro(models.Model):
    nombre = models.CharField(max_length=50)
    comentario = models.ManyToManyField(Comentario)

class Seccion(models.Model):
    nombre = models.CharField(max_length=50)
    foro = models.ManyToManyField(Foro)

class Imagenes_Viajes(models.Model):
    def __unicode__(self):
        return str(self.id)
    imagen = models.ImageField(upload_to='viajes')

class Viaje(models.Model):
    def __unicode__(self):
        return self.titulo
    titulo = models.CharField(max_length=50)
    historia = models.CharField(max_length=500)
    aprobado = models.BooleanField(default=False)
    imagen = models.ManyToManyField(Imagenes_Viajes)
