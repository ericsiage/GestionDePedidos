from django.http import request
from django.shortcuts import render, redirect
from .forms import formularioContacto
# Create your views here.


def contacto(request):
    
    formulario_contacto=formularioContacto
    
    if request.method=="POST":
        formulario_contacto=formularioContacto(data=request.POST)
        if formulario_contacto.is_valid():
            nombre=request.POST.get("nombre")
            email=request.POST.get("email")
            contenido=request.POST.get("contenido")

            return redirect("/contacto/?valido")

    return render(request,"contactoApp/contacto.html", {'formularioContacto': formulario_contacto})