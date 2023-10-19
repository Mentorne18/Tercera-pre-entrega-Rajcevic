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

# def cursos(request):
    
#     return render(request, "appCoder/cursos.html")

# def profesores(request):
    
#     return render(request, "appCoder/profesores.html")

def estudiantes(request):
    
    # return render(request, "appCoder/estudiantes.html")
    
    if request.method == "POST":
 
            miFormulario = EstudianteFormulario(request.POST) # Aqui me llega la informacion del html
            print(miFormulario)
 
            if miFormulario.is_valid():
                  informacion = miFormulario.cleaned_data
                  estudiante = Estudiante (nombre=informacion["nombre"], apellido=informacion["apellido"], email=informacion["email"])
                  estudiante.save()
                  return render(request, "AppCoder/index.html")
    else:
        miFormulario = EstudianteFormulario()
 
    return render(request, "AppCoder/estudiantes.html", {"miFormulario": miFormulario})
    

def entregables(request):

    # return render(request, "appCoder/entregables.html")
    
    if request.method == "POST":
 
            miFormulario = EntregableFormulario(request.POST) # Aqui me llega la informacion del html
            print(miFormulario)
 
            if miFormulario.is_valid():
                  informacion = miFormulario.cleaned_data
                  entregable = Entregables (nombre=informacion["nombre"], fechaDeEntrega=informacion("fecha de entrega"), entregado=informacion[" "])
                  entregable.save()
                  return render(request, "AppCoder/index.html")
    else:
        miFormulario = EntregableFormulario()
 
    return render(request, "AppCoder/entregables.html", {"miFormulario": miFormulario})

def cursos(request):
 
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
 
      return render(request, "AppCoder/cursos.html", {"miFormulario": miFormulario})
  
def profesores(request):
      
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
            
    return render(request, "AppCoder/profesores.html", {"miFormulario":miFormulario})


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


def leerProfesores(request):

      profesores = Profesor.objects.all() #trae todos los profesores

      contexto= {"profesores":profesores} 

      return render(request, "AppCoder/leerProfesores.html",contexto)


def eliminarProfesor(request, profesor_nombre):
 
    profesor = Profesor.objects.get(nombre=profesor_nombre)
    profesor.delete()
 
    # vuelvo al menú
    profesores = Profesor.objects.all()  # trae todos los profesores
 
    contexto = {"profesores": profesores}
 
    return render(request, "AppCoder/leerProfesores.html", contexto)


def editarProfesor(request, profesor_nombre):
    
    #recibe el nombre del profesor que vamos a modificar
    
    profesor = Profesor.objects.get(nombre=profesor_nombre)
    
    #Si es metodo POST hago lo mismo que el agregar
    
    if request.method == "POST":
        
        miFormulario = ProfesorFormulario(request.POST) #aca nos llega toda la info del html
        
        print(miFormulario)
        
        if miFormulario.is_valid():  #esto es "si pasa la verificacion de django"
            
            informacion = miFormulario.cleaned_data
            
            profesor.nombre = informacion["nombre"]
            profesor.apellido = informacion["apellido"]
            profesor.email = informacion["email"]
            profesor.profesion = informacion["profesion"]
            
            profesor.save()
            
            return render(request, "AppCoder/index.html") # Aca hacemos que vuelva al inicio despues de  editar
        
    #En caso de que no sea post:
    
    else:
        
         miFormulario = ProfesorFormulario(initial={"nombre": profesor.nombre, "apellido": profesor.apellido, "email": profesor.email, "profesion": profesor.profesion})
         
    #Aca vamos al html que si nos permite editar:
    
    return render(request,"AppCoder/editarProfesor.html", {"miFormulario":miFormulario, "profesor_nombre":profesor_nombre})