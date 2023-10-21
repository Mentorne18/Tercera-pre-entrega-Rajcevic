from typing import List
from django.shortcuts import redirect, render, HttpResponse
from django.http import HttpResponse
from .models import * #para traer Curso de models y usarlo en la validación de datos enviados.
from AppCoder.forms import *
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User





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
@login_required 
def inicio(request):
    
    avatares = Avatar.objects.filter(user=request.user.id)
    
    return render(request, "appCoder/index.html", {"url": avatares[0].imagen.url})

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


class CursoList(ListView):
    
    model= Curso
    template_name = "AppCoder/cursos_list.html"
    
class CursoDetalle(DetailView):
    
    model = Curso
    template_name = "AppCoder/curso_detalle.html"
    
class CursoCreacion(LoginRequiredMixin, CreateView):
    
    model = Curso
    success_url= "/AppCoder/curso/list"
    fields = ["nombre", "camada"]
    
class CursoUpdate(LoginRequiredMixin, UpdateView):
    
    model = Curso
    success_url = "/AppCoder/curso/list"
    fields = ["nombre", "camada"]
    
class CursoDelete(LoginRequiredMixin, DeleteView):
    
    model = Curso
    success_url = "AppCoder/curso/list"
    

def login_request(request):
    
    if request.method == "POST":
        form = AuthenticationForm(request, data= request.POST)
        
        if form.is_valid():
            usuario = form.cleaned_data.get("username")
            contra = form.cleaned_data.get("password")
            
            user = authenticate(username=usuario, password=contra)
            
            
            if user is not None:
                login(request, user)
                
                return render(request, "AppCoder/index.html", {"mensaje":f"Bienvenido {usuario}"})
            
            else:
                
                return render(request, "AppCoder/index.html", {"mensaje": "Error, datos incorrectos"})
            
        
        else:
            
                return render(request, "AppCoder/index.html", {"mensaje":"Error, formulario erroneo"})
            
    form = AuthenticationForm()
    
    return render(request, "AppCoder/login.html", {"form":form})


def register(request):
    
    if request.method == "POST":
        
        #form = UserCreationForm(request.POST)
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            
            username = form.cleaned_data["username"]
            form.save()
            return render(request, "AppCoder/index.html", {"mensaje":"Creacion de usuario exitosa, bienvenido"})
        
        
    else:
        
        #form = UserCreationForm()
        form =UserRegisterForm()
        
    return render(request,"AppCoder/registro.html", {"form":form})


@login_required
def editarPerfil(request):

      #Instancia del login
      usuario = request.user
     
      #Si es metodo POST hago lo mismo que el agregar
      if request.method == 'POST':
            miFormulario = UserEditForm(request.POST) 
            if miFormulario.is_valid():   #Si pasó la validación de Django

                  informacion = miFormulario.cleaned_data
            
                  #Datos que se modificarán
                  usuario.email = informacion['email']
                  usuario.password1 = informacion['password1']
                  usuario.password2 = informacion['password1']
                  usuario.save()

                  return render(request, "AppCoder/index.html") #Vuelvo al inicio o a donde quieran
      #En caso que no sea post
      else: 
            #Creo el formulario con los datos que voy a modificar
            miFormulario= UserEditForm(initial={ 'email':usuario.email}) 

      #Voy al html que me permite editar
      return render(request, "AppCoder/editarPerfil.html", {"miFormulario":miFormulario, "usuario":usuario})
  
  
@login_required
def agregarAvatar(request):
      if request.method == 'POST':

            miFormulario = AvatarFormulario(request.POST, request.FILES) #aca me llega toda la información del html

            if miFormulario.is_valid():   #Si pasó la validación de Django


                  u = User.objects.get(username=request.user)
                
                  avatar = Avatar (user=u, imagen=miFormulario.cleaned_data['imagen']) 
      
                  avatar.save()

                  return render(request, "AppCoder/index.html") #Vuelvo al inicio o a donde quieran

      else: 

            miFormulario= AvatarFormulario() #Formulario vacio para construir el html

      return render(request, "AppCoder/agregarAvatar.html", {"miFormulario":miFormulario})