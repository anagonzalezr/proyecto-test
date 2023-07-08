from django.contrib import admin
from .models import Artista, Producto, Motivo, Usuario, ContactoGeneral

# Register your models here.

admin.site.register(Artista)
admin.site.register(Producto)
admin.site.register(Motivo)
admin.site.register(Usuario)
admin.site.register(ContactoGeneral)