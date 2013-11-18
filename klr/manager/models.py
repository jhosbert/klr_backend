from django.db import models
from django.contrib.auth.models import User

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

class Viaje(models.Model):
	titulo = models.CharField(max_length=50)
	historia = models.CharField(max_length=500)
	aprobado = models.BooleanField(default=False)
	