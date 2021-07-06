from django.contrib import admin
from django.contrib.admin.options import ModelAdmin

# Register your models here.

from .models import Servicio

class servicioAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated') #solo de lectura



admin.site.register(Servicio,servicioAdmin)