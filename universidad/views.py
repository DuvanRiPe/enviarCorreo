from django.shortcuts import render

# Create your views here.
def FormularioContacto(request):
    return render(request, "formularioContacto.html")