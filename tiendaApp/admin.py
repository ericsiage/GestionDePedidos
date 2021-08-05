from django.contrib import admin

# Register your models here.
from .models import Categoria, Producto

class categoriaAdmin(admin.ModelAdmin): 
    readonly_fields=('created','updated') #solo de lectura

class productoAdmin(admin.ModelAdmin): 
    readonly_fields=('created','updated') #solo de lectura

admin.site.register(Categoria,categoriaAdmin)
admin.site.register(Producto,productoAdmin)