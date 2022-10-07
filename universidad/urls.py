from django.urls import path
from . import views
from .views import FormularioContacto
urlpatterns = [
    path('formularioContacto', views.FormularioContacto, name="formulario" )
]
