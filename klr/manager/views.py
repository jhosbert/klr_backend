from django.shortcuts import render, render_to_response
from django.contrib.auth import login, authenticate,logout
from django.template import RequestContext
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from manager.models import *
from manager.forms import *

def index(request):
    return render_to_response('index.html',context_instance = RequestContext(request))

def todos_viajes(request):
    viaje = Viaje.objects.all()
    return render_to_response('todos_viajes.html',{'viaje':viaje},context_instance = RequestContext(request))

@login_required(login_url='/')
def crear_viaje(request):
    if request.method == 'POST':
        formulario = ViajeForm(request.POST,request.FILES)
        if formulario.is_valid():
            titulo = formulario.cleaned_data['titulo']
            historia = formulario.cleaned_data['historia']
            lista_imagenes = request.FILES.getlist('lista_imagenes')
            viaje = Viaje.objects.create(titulo=titulo,historia=historia)
            viaje.save()
            for lista in lista_imagenes:
                imagen = Imagenes_Viajes.objects.create(imagen=lista)
                imagen.save()
                viaje.imagen.add(imagen)
            return HttpResponseRedirect('/viaje/crearViaje')
    formulario = ViajeForm()
    return render_to_response('crear_viaje.html',{'formulario':formulario},context_instance = RequestContext(request))

def Registro_usuario(request):
    if request.method == 'POST':
        formulario = RegistroUsuarioForm(request.POST,request.FILES)
        if formulario.is_valid():
            nombre = formulario.cleaned_data['nombre']
            contrasena = formulario.cleaned_data['contrasena']
            correo = formulario.cleaned_data['correo']
            user = User.objects.create_user(correo,correo,contrasena)
            user.first_name = nombre
            user.is_active = True
            user.save()
            return HttpResponseRedirect ('/')
    formulario = RegistroUsuarioForm()
    return render_to_response('registro_usuario.html',{'formulario':formulario},context_instance=RequestContext(request))

def detalles_viaje(request,id_viaje):
    viaje = Viaje.objects.get(id=id_viaje)
    return render_to_response('detalles_viaje.html',{'viaje':viaje},context_instance=RequestContext(request))

