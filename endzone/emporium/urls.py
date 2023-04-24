from django.contrib import admin
from django.urls import path
from django.conf.urls import url,include
from emporium.views import *
from .views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    url(r'^$', onboarding, name='onboarding'),

    path('iniciar_sesion/', iniciar_sesion, name="iniciar_sesion"),
]