from django.shortcuts import render
from django.http import HttpResponse
from .models import * #para traer Curso de models y usarlo en la validación de datos enviados.
from AppCoder.forms import *

# Create your views here.


# def inicio(request):
    
#     return HttpResponse("vista inicio")

# def cursos(request):
    
#     return HttpResponse("vista cursos")

# def profesores(request):
    
#     return HttpResponse("Vista profesores")

# def estudiantes(request):
    
#     return HttpResponse("Vista estudiantes")

# def entregables(request):
    
#     return HttpResponse("vista entregables")    ESTO YA NO VA PORQUE LO REEMPLAZAMOS POR EL RENDER DE LA PLANTILLA

def inicio(request):
    
    return render(request, "appCoder/index.html")

def cursos(request):
    
    return render(request, "appCoder/cursos.html")

def profesores(request):
    
    return render(request, "appCoder/profesores.html")

def estudiantes(request):
    
    return render(request, "appCoder/estudiantes.html")

def entregables(request):

    return render(request, "appCoder/entregables.html")

def cursoFormulario(request):
 
      if request.method == "POST":
 
            miFormulario = CursoFormulario(request.POST) # Aqui me llega la informacion del html
            print(miFormulario)
 
            if miFormulario.is_valid():
                  informacion = miFormulario.cleaned_data
                  curso = Curso(nombre=informacion["curso"], camada=informacion["camada"])
                  curso.save()
                  return render(request, "AppCoder/index.html")
      else:
            miFormulario = CursoFormulario()
 
      return render(request, "AppCoder/cursoFormulario.html", {"miFormulario": miFormulario})
  
def profesorFormulario(request):
      
    if request.method == "POST":
          
          miFormulario = ProfesorFormulario(request.POST)
          
          print(miFormulario)
          
          if miFormulario.is_valid():  #esta es la validación que usamos tambien en el otro formulario por si ponen algun dato mal

                informacion = miFormulario.cleaned_data
                
                profesor = Profesor (nombre=informacion["nombre"], apellido=informacion["apellido"], email=informacion["email"], profesion=informacion["profesion"])
                
                profesor.save()
                
                return render(request, "AppCoder/index.html") #esta es la pagina a la que vuelve despues de completar el formulario
            
            
    else:
        
        miFormulario= ProfesorFormulario() #formulario vacio para construir el html (esto revisarlo)
            
    return render(request, "AppCoder/profesorFormulario.html", {"miFormulario":miFormulario})


def busquedaCamada(request):
    
    return render(request, "AppCoder/busquedaCamada.html")

def buscar(request):
    
    #respuesta = f"Estoy buscando la camada N°: {request.GET['camada'] }"
    
    if request.GET["camada"]:
        
        camada = request.GET["camada"]
        cursos = Curso.objects.filter(camada__icontains=camada)
        
        return render(request, "AppCoder/resultadosBusqueda.html", {"cursos":cursos, "camada":camada})
    
    else:
        
        respuesta = "No enviaste datos"
    
    return HttpResponse(respuesta)