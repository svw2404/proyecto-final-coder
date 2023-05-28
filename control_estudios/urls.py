"""
URL configuration for sistema_coder project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from control_estudios.views import listar_articulo, eliminar_comentario, crear_articulo, crear_comentario, buscar_articulo,\
    eliminar_articulo, editar_articulo, ver_mas, EstudianteListView, EstudianteCreateView,\
    EstudianteDetailView, EstudianteUpdateView, EstudianteDeleteView


urlpatterns = [
    # URLS de cursos
    path("articulo/", listar_articulo, name="lista_articulo"),
    path("crear-articulo/", crear_articulo, name="crear_articulo"),
    path("buscar-articulo/", buscar_articulo, name="buscar_articulo"),
    path("eliminar-articulo/<int:id>/", eliminar_articulo, name="eliminar_articulo"),
    path("editar-articulo/<int:id>/", editar_articulo, name="editar_articulo"),
    path("ver-mas/<int:id>/", ver_mas, name="ver_mas"),
    path("crear_comentario/<int:id>/", crear_comentario, name="crear_comentario"),
    path("eliminar-comentario/<int:id_comentario>/<int:id_articulo>/", eliminar_comentario, name="eliminar_comentario"),
    # URLS de estudiantes
    path("estudiantes/", EstudianteListView.as_view(), name="lista_estudiantes"),
    path('estudiantes/<int:pk>/', EstudianteDetailView.as_view(), name="ver_estudiante"),
    path('crear-estudiante/', EstudianteCreateView.as_view(), name="crear_estudiante"),
    path('editar-estudiante/<int:pk>/', EstudianteUpdateView.as_view(), name="editar_estudiante"),
    path('eliminar-estudiante/<int:pk>/', EstudianteDeleteView.as_view(), name="eliminar_estudiante"),
]
