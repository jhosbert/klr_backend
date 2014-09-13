#encoding:utf-8
from django.forms import ModelForm
from django import forms
from django.db import models
from manager.models import *
from foros.models import *
from django.contrib.auth.models import User
from django.contrib.admin.widgets import AdminDateWidget
from django.forms.extras.widgets import SelectDateWidget
from django.forms.widgets import CheckboxSelectMultiple

class nuevoForoForm(forms.Form):
    nombre = forms.CharField(max_length=20)

class nuevoComentarioForm(forms.Form):
    texto = forms.CharField(max_length=400, label='Comentario', widget=forms.TextInput(attrs={'placeholder': 'Realizar un comentario'}))