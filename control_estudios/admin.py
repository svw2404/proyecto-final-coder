from django.contrib import admin

from control_estudios.models import Curso, Estudiante, Profesor, Entregable, Comentario, Articulo


admin.site.register(Curso)
admin.site.register(Estudiante)
admin.site.register(Profesor)
admin.site.register(Entregable)
admin.site.register(Articulo)
admin.site.register(Comentario)