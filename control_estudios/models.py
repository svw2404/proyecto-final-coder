from django.db import models
from django.contrib.auth.models import User
from datetime import date

class Curso(models.Model):
    nombre = models.CharField(max_length=64)  # Equivalente de str
    comision = models.IntegerField()  # Equivalent de int
    creador = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.nombre} | {self.comision}"


class Estudiante(models.Model):
    apellido = models.CharField(max_length=256)
    nombre = models.CharField(max_length=256)
    email = models.EmailField(blank=True)
    telefono = models.CharField(max_length=20, blank=True)
    dni = models.CharField(max_length=32)
    fecha_nacimiento = models.DateField(null=True)
    creador = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.nombre}, {self.apellido}"


class Profesor(models.Model):
    apellido = models.CharField(max_length=256)
    nombre = models.CharField(max_length=256)
    dni = models.CharField(max_length=32)
    email = models.EmailField(blank=True)
    fecha_nacimiento = models.DateField(null=True, blank=True)
    profesion = models.CharField(max_length=128)
    bio = models.TextField(blank=True)
    creador = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name_plural = "profesores"

    def __str__(self):
        return f"{self.nombre}, {self.apellido}"


class Entregable(models.Model):
    nombre = models.CharField(max_length=256)
    fecha_entrega = models.DateTimeField(auto_now_add=True)
    esta_aprobado = models.BooleanField(default=False)  # equivalente a bool (True, False)



class Articulo(models.Model):
    titulo = models.CharField(max_length=256)
    subtitulo = models.CharField(max_length=256)
    cuerpo = models.TextField()
    autor = models.CharField(max_length=64)
    fecha = models.DateField(default=date.today)
    imagen = models.ImageField(upload_to='articulos', null=True, blank=True)

class Comentario(models.Model):
    articulo_id = models.IntegerField()
    comentador = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    cuerpo = models.TextField()
    fecha = models.DateField(default=date.today)