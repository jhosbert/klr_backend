#encoding:utf-8
from django.forms import ModelForm
from django import forms
from manager.models import Viaje

class ViajeForm(forms.ModelForm):
	class Meta:
		model = Viaje
        exclude = {'aprobado'}

	"""def handle_uploaded_file(self,file):
		#print type(file), "file.name=",file.name
		#print dir(file)
		destination = open(MEDIA_URL + '/images/'+file.name, 'wb+')
		for chunk in file.chunks():
			destination.write(chunk)"""

class RegistroUsuarioForm(forms.ModelForm):
	nombre = forms.CharField(max_length = 100)
	contrasena = 
	correo =
