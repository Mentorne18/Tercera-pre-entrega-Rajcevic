from django.contrib import admin
from .models import * #importamos todos los modelos de models.py

# Register your models here.

admin.site.register(Curso)

admin.site.register(Estudiante)

admin.site.register(Profesor)

admin.site.register(Entregables)
