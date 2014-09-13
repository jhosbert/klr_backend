from django.shortcuts import render, render_to_response
from django.contrib.auth import login, authenticate,logout
from django.template import RequestContext
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from manager.models import *
from foros.models import *
from manager.forms import *
from foros.forms import *

def todos_foros(request,id_seccion):
    seccion = Seccion.objects.get(id=int(id_seccion))
    return render_to_response('foros/todos_foros.html',{'seccion':seccion,'id_seccion':id_seccion},context_instance = RequestContext(request))

def todas_secciones(request):
    secciones = Seccion.objects.all()
    for sec in secciones:
        print 'jhy'
        print sec.foro.all().count()
    return render_to_response('foros/todas_secciones.html',{'secciones':secciones},context_instance=RequestContext(request))

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
    return render_to_response('foros/nuevoForo.html',{'formulario':formulario},context_instance=RequestContext(request))

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
    return render_to_response('foros/detallesForo.html',{'foro':foro,'comentarios':comentarios,'formulario':formulario},context_instance=RequestContext(request))