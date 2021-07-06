from django.shortcuts import render, HttpResponse
from .models import Servicio
# Create your views here.

def servicios(request):
    servicios=Servicio.objects.all()#se importan todos los servicios dentro de la variable

    return render(request,"servicios/servicios.html", {"servicios": servicios}) #se muestran los servicios
