from .models import Producto, Categoria
from django.shortcuts import render

# Create your views here.


def tienda(request):
    productos=Producto.objects.all()
    return render(request, "tiendaApp/tienda.html", {"productos": productos})