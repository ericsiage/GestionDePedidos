from django.db import models

# Create your models here.
#mapeo ORM

class Servicio(models.Model):
    titulo=models.CharField(max_length=30)
    contenido=models.CharField(max_length=30)
    imagen=models.ImageField(upload_to='servicios') #subir las imagenes en carpeta 'servicios'
    created=models.DateTimeField(auto_now_add=True) #fecha de creacion del Servicio
    updated=models.DateTimeField(auto_now_add=True)

    class Meta: #meta class contiene metadatos
        verbose_name='servicio' #especificamos el nombbre que tendra el servicio en la base de datos
        verbose_name_plural='servicios' 

    def __str__(self):
        return self.titulo