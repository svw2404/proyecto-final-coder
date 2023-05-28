from django.contrib import admin

from articulos.models import Comentario, Articulo

admin.site.register(Articulo)
admin.site.register(Comentario)