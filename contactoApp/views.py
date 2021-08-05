from django.http import request
from django.shortcuts import render, redirect
from .forms import formularioContacto
from django.core.mail import EmailMessage


# Create your views here.


def contacto(request):
    
    formulario_contacto=formularioContacto
    
    if request.method=="POST":
        formulario_contacto=formularioContacto(data=request.POST)
        if formulario_contacto.is_valid():
            nombre=request.POST.get("nombre")
            email=request.POST.get("email")
            asunto=request.POST.get("asunto")
            contenido=request.POST.get("contenido")

            email=EmailMessage(asunto, "El usuario con nombre: {} con la direccion: {} te escribe: {}".format(nombre, email, contenido),"",["ericsiage@gmail.com"],reply_to=[email])

            try:
                email.send()
                return redirect("/contacto/?valido")
            except:
                return redirect("/contacto/?novalido")

    return render(request,"contactoApp/contacto.html", {'formularioContacto': formulario_contacto})