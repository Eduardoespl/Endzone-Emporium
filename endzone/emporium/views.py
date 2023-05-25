from django.shortcuts import render
from .forms import *
from .models import *
from multiprocessing import context
from django.shortcuts import redirect
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.models import User
from django.http import JsonResponse
import json


def onboarding(request):
    template='hola.html'
    return render(request, template)

def cascos_page(request):
    template='cascos.html'
    return render(request, template)

def iniciar_sesion(request):
    template='login.html'
    if request.user.is_authenticated:
        return redirect('dashboard')
    else:
        if request.method == 'POST':
            username=request.POST.get('username')
            password=request.POST.get('password')
            print(username)
            print(password)

            user=authenticate(request,username=username,password=password)
            if user is not None:
                login(request,user)
                return redirect('dashboard')
            else:
                messages.info(request,'Usuario o contraseña son incorrectos')
            
    context={

    }
    return render(request, template,context)

def registro(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    else:
        form = CreateUserForm()
        if request.method=='POST':
            form= CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user=form.cleaned_data.get('username')
                messages.success(request,'La cuenta ha sido creada para:'+ user)
                return redirect('iniciar_sesion')

        context={'form':form}
        return render(request,'register.html',context)

def dashboard(request):
    template='dashboard.html'
    return render(request, template)

def username(request):
    user=request.user
    return HttpResponse(user)

""" Codigo que obtenga los valores del casco desde la base de datos y regrese un json con los valores """

def obtener_cascos(request):
    casco = cascos.objects.all()
    casco_list = list(casco.values())  # Convert queryset to a list of dictionaries
    casco_json = json.dumps(casco_list)# Serialize the list to JSON format
    return JsonResponse(casco_json, safe=False)

def guardar_cascos(request):
    if request.method == 'POST':
        form = cascosForm(request.POST, request.FILES)
        if form.is_valid():
            print("es valido")
            imagen = request.FILES['image']
            marca = request.POST['marca']
            modelo = request.POST['modelo']
            precio = request.POST['precio']
            talla = request.POST['talla']
            casco = cascos(image=imagen, marca=marca, modelo=modelo, precio=precio, talla=talla)
            casco.save()
            return redirect('cascos_page')
        else:
            print("***********")
            print(form.errors)
            print("no es valido")
    else:
        form = cascosForm()
    context = {'form': form}
    return render(request, 'post_casco.html', context)
    
def post_casco(request):
    template='post_casco.html'
    return render(request, template)

def eliminar_casco(request):
    if request == 'POST':
        casco = cascos()
        casco.marca = request.POST.get('marca')
        casco.modelo = request.POST.get('modelo')
        casco.precio = request.POST.get('precio')
        casco.talla = request.POST.get('talla')
        casco.image = request.POST.get('image')
        casco.delete()
        return render(request, 'cascos.html')
