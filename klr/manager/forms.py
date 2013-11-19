#encoding:utf-8
from django.forms import ModelForm
from django import forms
from manager.models import Viaje

class ViajeForm(ModelForm):
	class Meta:
		model = Viaje

	"""def handle_uploaded_file(self,file):
		#print type(file), "file.name=",file.name
		#print dir(file)
		destination = open(MEDIA_URL + '/images/'+file.name, 'wb+')
		for chunk in file.chunks():
			destination.write(chunk)"""