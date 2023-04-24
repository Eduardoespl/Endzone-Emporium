from django.shortcuts import render
from .forms import *
from .models import *
from multiprocessing import context
from django.shortcuts import redirect
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.contrib.auth import authenticate, login
from django.contrib import messages

def onboarding(request):
    template='hola.html'
    return render(request, template)

def iniciar_sesion(request):
    template='login.html'
    if request.user.is_authenticated:
        return redirect('onboarding')
    else:
        if request.method == 'POST':
            username=request.POST.get('username')
            password=request.POST.get('password')
            print(username)
            print(password)

            user=authenticate(request,username=username,password=password)
            if user is not None:
                login(request,user)
                return redirect('onboarding')
            else:
                messages.info(request,'Usuario o contraseña son incorrectos')
            
    context={

    }
    return render(request, template,context)