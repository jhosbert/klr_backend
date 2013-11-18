#encoding:utf-8
from django.forms import ModelForm
from django import forms
from manager.models import Viaje

class ViajeForm(ModelForm):
	class Meta:
		model = Viaje