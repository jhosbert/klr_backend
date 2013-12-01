#encoding:utf-8
from django.forms import ModelForm
from django import forms
from django.db import models
from manager.models import *
from django.contrib.auth.models import User
from django.contrib.admin.widgets import AdminDateWidget
from django.forms.extras.widgets import SelectDateWidget
from django.forms.widgets import CheckboxSelectMultiple

class ViajeForm(forms.Form):
    titulo = forms.CharField(max_length=50)
    historia = forms.CharField(max_length=500)

class RegistroUsuarioForm(forms.ModelForm):
    nombre = forms.CharField(max_length = 100)
    contrasena = forms.CharField(max_length = 32, widget = forms.PasswordInput)
    correo = forms.EmailField(help_text='A valid email address, please.')

class nuevoForoForm(forms.Form):
    nombre = forms.CharField(max_length=20)

class nuevoComentarioForm(forms.Form):
    texto = forms.CharField(max_length=400)
