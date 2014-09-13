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
    fecha = models.DateTimeField(auto_now=True)

class Foro(models.Model):
    def __unicode__(self):
        return str(self.nombre)
    nombre = models.CharField(max_length=50)
    comentario = models.ManyToManyField(Comentario,blank=True,null=True)

class Seccion(models.Model):
    def __unicode__(self):
        return str(self.nombre)
    nombre = models.CharField(max_length=50)
    foro = models.ManyToManyField(Foro,blank=True,null=True)