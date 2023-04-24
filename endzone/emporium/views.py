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