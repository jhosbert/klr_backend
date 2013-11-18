from django.shortcuts import render, render_to_response
from django.contrib.auth import login, authenticate,logout
from django.template import RequestContext
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponseRedirect 
from manager.models import *
from manager.forms import *

# Create your views here.
def loginUser(request):
	if request.method == 'POST':
		formulario = AuthenticationForm(request.POST)
		username = request.POST['username']
		password = request.POST['password']
		access = authenticate(username=username,password=password)

		print access
		if access is not None:
			if access.is_active:
				login(request,access)
				return HttpResponseRedirect('/login')
		formulario = AuthenticationForm()
		print 'error'
		return render_to_response('login.html',{'formulario':formulario,'mensaje':'eeeeeeeeeeerrrrorrr'},context_instance = RequestContext(request))
	
	else:
		formulario = AuthenticationForm()
	return render_to_response('login.html',{'formulario':formulario},context_instance = RequestContext(request))

def todos_foros(request,id_seccion):
	seccion = Seccion.objects.get(id=id_seccion)
	return render_to_response('todos_foros.html',{'seccion':seccion},context_instance = RequestContext(request))	

def todos_viajes(request):
	viaje = Viaje.objects.all()
	print viaje[1].titulo
	return render_to_response('todos_viajes.html',{'viaje':viaje},context_instance = RequestContext(request))

def crear_viaje(request):
	if request.method=='POST':
		formulario = ViajeForm(request.POST,request.FILES)
		if formulario.is_valid():
			formulario.save()
			return HttpResponseRedirect('/viaje/crearViaje')
	else:
		formulario = ViajeForm()
		return render_to_response('crear_viaje.html',{'formulario':formulario},context_instance=RequestContext(request))