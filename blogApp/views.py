from django.shortcuts import render
from blogApp.models import Categoria, Post
# Create your views here.

def blog(request):
    posts=Post.objects.all()
    return render(request,"blogApp/blog.html", {"posts": posts}) #argumento posts para mostrar los modelos en el template