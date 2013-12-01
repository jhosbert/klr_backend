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

def loginUser(request):
    if request.method == 'POST':
        formulario = AuthenticationForm(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        access = authenticate(username=username,password=password)

        if access is not None:
            if access.is_active:
                login(request,access)
                return HttpResponseRedirect('/')
        else:
            formulario = AuthenticationForm()
            return render_to_response('login.html',{'formulario':formulario,'mensaje':'error al iniciar sesion'},context_instance = RequestContext(request))
    formulario = AuthenticationForm()
    return render_to_response('login.html',{'formulario':formulario},context_instance = RequestContext(request))

def todos_foros(request,id_seccion):
    seccion = Seccion.objects.get(id=int(id_seccion))
    return render_to_response('todos_foros.html',{'seccion':seccion,'id_seccion':id_seccion},context_instance = RequestContext(request))

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

def todas_secciones(request):
    secciones = Seccion.objects.all()
    return render_to_response('todas_secciones.html',{'secciones':secciones},context_instance=RequestContext(request))

def nuevoForo(request,id_seccion):
    if request.method == 'POST':
        formulario = nuevoForoForm(request.POST,request.FILES)
        if formulario.is_valid():
            nombre = formulario.cleaned_data['nombre']
            foro = Foro.objects.create(nombre=nombre)
            foro.save()

            #ManyToMany
            seccion = Seccion.objects.get(id = int(id_seccion))
            seccion.foro.add(foro)
            seccion.save()
            return HttpResponseRedirect('/todos_foros/' + id_seccion)

    formulario = nuevoForoForm()
    return render_to_response('nuevoForo.html',{'formulario':formulario},context_instance=RequestContext(request))

def detallesForo(request,id_foro):
    foro = Foro.objects.get(id=int(id_foro))
    if request.method == 'POST':
        formulario = nuevoComentarioForm(request.POST,request.FILES)
        if formulario.is_valid():
            texto = formulario.cleaned_data['texto']
            usuario = request.user
            coment = Comentario.objects.create(texto=texto,usuario=usuario)
            coment.save()
            foro.comentario.add(coment)
            foro.save()
            return HttpResponseRedirect('/detallesForo/' + id_foro)

    comentarios = foro.comentario.all().order_by('-fecha')
    formulario = nuevoComentarioForm()
    return render_to_response('detallesForo.html',{'foro':foro,'comentarios':comentarios,'formulario':formulario},context_instance=RequestContext(request))