from django.shortcuts import render
from django.http import HttpResponse
from .models import Proyecto

# Create your views here.

def home(request):

    titulo = "Proyectos Presentados"

    data = {
        "titulo" : titulo,

    }

    return render(request, 'core/home.html', data)

def estudiantes(request):

    titulo = "Ingresar o Modificar Proyecto"

    data = {
        "titulo" : titulo,
    }

    return render(request, 'core/estudiantes.html',data)

def profesores(request):

    titulo = "Proyectos Presentados"

    data = {
        "titulo" : titulo,
    }

    return render(request, 'core/profesores.html', data)

def nuevo_proyecto(request):
    if(request.POST):

        id = request.POST['intID']
        nombre = request.POST['txtNombre']
        tema = request.POST['cboTema']
        profesor = request.POST['txtProfesor']
        estudiante = request.POST['txtEstudiante']

        proyecto = Proyecto()
        proyecto.id = id
        proyecto.nombre = nombre
        proyecto.tema = tema
        proyecto.profesor = profesor
        proyecto.estudiante = estudiante

        proyecto.save()

    return render(request, 'core/estudiantes.html')
