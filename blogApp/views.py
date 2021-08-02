from django.shortcuts import render
from blogApp.models import Categoria, Post
# Create your views here.

def blog(request):
    posts=Post.objects.all() #objetos del modelo Post.
    return render(request,"blogApp/blog.html", {"posts": posts}) #argumento posts para mostrar los modelos en el template

def categoria(request, categoria_id): #segundo argumento es el id de la categoria para poder utilizarlo
    
    categoria=Categoria.objects.get(id=categoria_id) #get id de categoria_id
    posts=Post.objects.filter(categoria=categoria)#filtro para mostrar
    
    return render(request, "blogApp/categoria.html", {"categoria":categoria, "posts":posts}) #argumento para mostrar los modelos en el template
