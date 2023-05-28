from django import forms
from .models import Articulo
import os
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.core.files.storage import FileSystemStorage
from django.conf import settings

class ArticuloFormulario(forms.ModelForm):
    titulo = forms.CharField(required=True, max_length=256, widget=forms.Textarea(attrs={'rows': 1,'style': 'width: 800px;'}))
    subtitulo = forms.CharField(required=True, max_length=256, widget=forms.Textarea(attrs={'rows': 2,'style': 'width: 800px;'}))
    cuerpo = forms.CharField(required=True, max_length=65535, widget=forms.Textarea(attrs={'rows': 8, 'style': 'width: 800px;'}))
    imagen = forms.ImageField(required=False)

    def save(self, commit=True):
        articulo = super().save(commit=False)
        imagen = self.cleaned_data.get('imagen')

        if imagen:
            # Set the image file path
            articulo.imagen = 'articulos/' + imagen.name

            # Save the image file to the desired directory
            with open('media/' + articulo.imagen, 'wb') as file:
                for chunk in imagen.chunks():
                    file.write(chunk)

        if commit:
            articulo.save()
        
        return articulo

    class Meta:
        model = Articulo
        fields = ['titulo', 'subtitulo', 'cuerpo', 'imagen']

class ComentarioFormulario(forms.Form):
    cuerpo = forms.CharField(
        required=True,
        max_length=65535,
        widget=forms.Textarea(attrs={'rows': 8, 'style': 'width: 800px'})
    )
