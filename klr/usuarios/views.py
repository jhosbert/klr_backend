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
        print 'post'
        formulario = AuthenticationForm(request.POST)
        if formulario.is_valid:
            username = request.POST['username']
            password = request.POST['password']
            access = authenticate(username=username,password=password)

            if access is not None:
                if access.is_active:
                    login(request,access)
                    print 'tiene acceso'
                    return HttpResponseRedirect('/')
            else:
                return render_to_response('usuarios/login.html',{'formulario':formulario,'fail':True},context_instance = RequestContext(request))
        else:
            print 'no valido'
            return render_to_response('usuarios/login.html',{'formulario':formulario,'fail':True},context_instance = RequestContext(request))
    else:
        print 'else'
        formulario = AuthenticationForm()
    return render_to_response('usuarios/login.html',{'formulario':formulario},context_instance = RequestContext(request))

def cerrarSesion(request):
    logout(request)
    return HttpResponseRedirect('/')