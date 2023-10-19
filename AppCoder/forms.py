from django import forms

class CursoFormulario(forms.Form):
    
    #especificar los campos
    
    curso = forms.CharField()
    camada = forms.IntegerField()
    
    
class ProfesorFormulario(forms.Form):
    
    nombre= forms.CharField(max_length=30)
    apellido= forms.CharField(max_length=30)
    email= forms.EmailField()
    profesion= forms.CharField(max_length=30)
    

class EstudianteFormulario(forms.Form):
    
    nombre= forms.CharField(max_length=30)
    apellido= forms.CharField(max_length=30)
    email= forms.EmailField()
    
    
class EntregableFormulario(forms.Form):
    
    nombre = forms.CharField(max_length=30)
    fecha_De_Entrega = forms.DateField()
    entregado = forms.BooleanField() 