from django.contrib import admin
from django.urls import path
from django.conf.urls import url,include
from emporium.views import *
from .views import *
from django.contrib.auth.views import LogoutView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', onboarding, name='onboarding'),

    path('iniciar_sesion/', iniciar_sesion, name="iniciar_sesion"),
    path('registrar/', registro, name="registrar"),
    path('dashboard/', dashboard, name="dashboard"),
    path('logout/', LogoutView.as_view(), name="logout"),
    path('cascos_page/', cascos_page, name="cascos_page"),

    path('obtener_cascos/', obtener_cascos, name='obtener_cascos'),
    path('guardar_cascos/', guardar_cascos, name='guardar_cascos'),
    path('post_casco/', post_casco, name='post_casco'),
    path('eliminar_casco/', eliminar_casco, name='eliminar_casco'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)