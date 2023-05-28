from django.contrib import admin
from django.urls import path

from articulos.views import listar_articulo, eliminar_comentario, crear_articulo, crear_comentario, buscar_articulo,\
    eliminar_articulo, editar_articulo, ver_mas


urlpatterns = [
    path("pages/", listar_articulo, name="lista_articulo"),
    path("crear-articulo/", crear_articulo, name="crear_articulo"),
    path("buscar-articulo/", buscar_articulo, name="buscar_articulo"),
    path("eliminar-articulo/<int:id>/", eliminar_articulo, name="eliminar_articulo"),
    path("editar-articulo/<int:id>/", editar_articulo, name="editar_articulo"),
    path("pages/<int:id>/", ver_mas, name="ver_mas"),
    path("crear_comentario/<int:id>/", crear_comentario, name="crear_comentario"),
    path("eliminar-comentario/<int:id_comentario>/<int:id_articulo>/", eliminar_comentario, name="eliminar_comentario")
]
