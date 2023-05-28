from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from articulos.forms import ArticuloFormulario, ComentarioFormulario
from articulos.models import Articulo, Comentario

@login_required
def editar_articulo(request, id):
    articulo = Articulo.objects.get(id=id)
    if request.method == "POST":
        formulario = ArticuloFormulario(request.POST, request.FILES)

        if formulario.is_valid():
            data = formulario.cleaned_data
            articulo.titulo = data["titulo"]
            articulo.subtitulo = data["subtitulo"]
            articulo.cuerpo = data["cuerpo"]
            if data["imagen"] != None:
                articulo.imagen = data["imagen"]
            articulo.save()

            url_exitosa = reverse('lista_articulo')
            return redirect(url_exitosa)
    else:  # GET
        inicial = {
            'titulo': articulo.titulo,
            'subtitulo': articulo.subtitulo,
            'cuerpo': articulo.cuerpo,
            'imagen': articulo.imagen,
        }
        formulario = ArticuloFormulario(initial=inicial)
    return render(
        request=request,
        template_name='control_estudios/formulario_articulo.html',
        context={'formulario': formulario},
    )

@login_required
def crear_articulo(request):
    if request.method == "POST":
        formulario = ArticuloFormulario(request.POST, request.FILES)  
        if formulario.is_valid():
            data = formulario.cleaned_data
            titulo = data["titulo"]
            subtitulo = data["subtitulo"]
            cuerpo = data["cuerpo"]
            imagen = data["imagen"]
            autor = request.user
            articulo = Articulo(titulo=titulo, subtitulo=subtitulo, cuerpo=cuerpo, autor=autor, imagen=imagen)
            articulo.save()

            url_exitosa = reverse('lista_articulo')
            return redirect(url_exitosa)
    else:
        formulario = ArticuloFormulario()
    http_response = render(
        request=request,
        template_name='control_estudios/formulario_articulo.html',
        context={'formulario': formulario}
    )
    return http_response

@login_required
def eliminar_articulo(request, id):
    articulo = Articulo.objects.get(id=id)
    if request.method == "POST":
        articulo.delete()
        url_exitosa = reverse('lista_articulo')
        return redirect(url_exitosa)

def listar_articulo(request):
    contexto = {
        "articulos": Articulo.objects.all(),
    }

    http_response = render(
        request=request,
        template_name='control_estudios/lista_articulo.html',
        context=contexto,
    )
    return http_response

def ver_mas(request, id):
    if request.method == "POST":
        formulario = ComentarioFormulario(request.POST)
        if formulario.is_valid():
            data = formulario.cleaned_data
            cuerpo = data["cuerpo"]
            comentador = request.user
            comentario = Comentario(articulo_id=id, cuerpo=cuerpo, comentador=comentador)
            comentario.save()

            url_exitosa = reverse('ver_mas', args=[id]) 
            return redirect(url_exitosa)
    else:
        formulario = ComentarioFormulario()

    comentario_filtrado = Comentario.objects.filter(articulo_id=id)
    articulo = Articulo.objects.get(id=id)
    contexto = {
        "articulo": articulo,
        "comments": comentario_filtrado,
        "formulario": formulario
    }
    return render(
        request=request,
        template_name='control_estudios/ver_mas.html',
        context=contexto,
    )


def buscar_articulo(request):
    if request.method == "POST":
        data = request.POST
        busqueda = data["busqueda"]
        articulos = Articulo.objects.filter(titulo__contains=busqueda)
        contexto = {
            "articulos": articulos,
            "reciente": busqueda
        }
        http_response = render(
            request=request,
            template_name='control_estudios/lista_articulo.html',
            context=contexto,
        )
        return http_response


@login_required
def crear_comentario(request, id):
    if request.method == "POST":
        formulario = ComentarioFormulario(request.POST)
        if formulario.is_valid():
            data = formulario.cleaned_data
            cuerpo = data["cuerpo"]
            comentador = request.user
            comentario = Comentario(articulo_id=id, cuerpo=cuerpo, comentador=comentador)
            comentario.save()

            url_exitosa = reverse('ver_mas', args=[id]) 
            return redirect(url_exitosa)
    else:
        formulario = ComentarioFormulario()

    http_response = render(
        request=request,
        template_name='control_estudios/ver_mas.html',
        context={'formulario': formulario}
    )
    return http_response

@login_required
def eliminar_comentario(request, id_comentario, id_articulo):
    comentario = Comentario.objects.get(id=id_comentario)
    if request.method == "POST":
        comentario.delete()
        url_exitosa = reverse('ver_mas', args=[id_articulo])
        return redirect(url_exitosa)