from multiprocessing.sharedctypes import Value
from urllib import request
from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'Nombre de usuario'}),
            'password1': forms.PasswordInput(attrs={'placeholder': 'Contraseña'}),
            'password2': forms.PasswordInput(attrs={'placeholder': 'Confirmar contraseña'}),
        }

class cleatsForm(forms.ModelForm):
    class Meta:
        model = cleats
        fields = '__all__'

class cascosForm(forms.ModelForm):
    class Meta:
        model = cascos
        fields = '__all__'

class accesoriosForm(forms.ModelForm):
    class Meta:
        model = accesorios
        fields = '__all__'