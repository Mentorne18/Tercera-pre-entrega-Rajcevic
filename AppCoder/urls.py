
from django.urls import path

from AppCoder import views

urlpatterns = [
    
    path("", views.inicio, name="Inicio"), #Esta es nuestra 1er view
    path("cursos", views.cursos, name="Cursos"),
    path("profesores", views.profesores, name="Profesores"),
    path("estudiantes", views.estudiantes, name="Estudiantes"),
    path("entregables", views.entregables, name="Entregables"),
    #path("cursoFormulario/", views.cursoFormulario, name="cursoFormulario"),
    #path("profesorFormulario/", views.profesorFormulario, name="ProfesorFormulario"),
    path("busquedaCamada/", views.busquedaCamada, name="BusquedaCamada"),
    path("buscar/", views.buscar),
    path('leerProfesores', views.leerProfesores, name = "LeerProfesores"),
    path('eliminarProfesor/<profesor_nombre>/', views.eliminarProfesor, name="EliminarProfesor"),
    path('editarProfesor/<profesor_nombre>/', views.editarProfesor, name="EditarProfesor"),
]