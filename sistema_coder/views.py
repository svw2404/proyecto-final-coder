from datetime import datetime

from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    contexto = {}
    http_response = render(
        request=request,
        template_name='articulos/home.html',
        context=contexto,
    )
    return http_response

def about(request):
    contexto = {}
    http_response = render(
        request=request,
        template_name='articulos/about.html',
        context=contexto,
    )
    return http_response
