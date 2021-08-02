from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Categoria(models.Model):
    nombre=models.CharField(max_length=50)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)

    class Meta: #meta class contiene metadatos
        verbose_name='categoria' #especificamos el nombbre que tendra el servicio en la base de datos
        verbose_name_plural='categorias' 

    def __str__(self):
        return self.nombre

class Post(models.Model):
    titulo=models.CharField(max_length=50)
    contenido=models.CharField(max_length=30)
    imagen=models.ImageField(upload_to='blog', null=True, blank=True) #subir las imagenes en carpeta 'media/blog'
    autor=models.ForeignKey(User, on_delete=models.CASCADE)#relacion uno a muchos, un usuario puede hacer varios post pero un mismo post no puede ser de varios usuarios.on_delete=CASCADE, cuando el user se elimina, tambien se eliminan los post.
    categoria=models.ManyToManyField(Categoria) #relacion muchos a muchos un post puede tener muchas categorias y las categorias pueden estar en muchos post. 
    created=models.DateTimeField(auto_now_add=True) #fecha de creacion del blog
    updated=models.DateTimeField(auto_now_add=True)

    class Meta: #meta class contiene metadatos
        verbose_name='post' #especificamos el nombbre que tendra el blog en la base de datos
        verbose_name_plural='posts'  #nombre en plural.

    def __str__(self):
        return self.titulo