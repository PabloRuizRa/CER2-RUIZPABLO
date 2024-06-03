from django.db import models

# Create your models here.


class Estudiante(models.Model):
    rut = models.CharField(max_length=10, primary_key=True, verbose_name="Rut")
    nombre = models.CharField(max_length=50, verbose_name="Nombre")

    def __str__(self) -> str:
        return self.nombre

class Profesor(models.Model):
    rut = models.CharField(max_length=10, primary_key=True, verbose_name="Rut")
    nombre = models.CharField(max_length=50, verbose_name="Nombre")

    def __str__(self) -> str:
        return self.nombre
    
temas = [
    ("0","Economía"),
    ("1","Educación"),
    ("2","Social"),
    ("3","Ciencias"),
    ("4","Ecológico"),
    ("5","Innovación"),
]

class Proyecto(models.Model):
    id = models.CharField(max_length=20, primary_key=True, verbose_name="Id")
    nombre = models.CharField(max_length=100, verbose_name="Nombre")
    tema = models.CharField(max_length=100, verbose_name="Tema", choices=temas)
    profesor = models.ForeignKey(Profesor, on_delete=models.CASCADE, null=True, blank=True)
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.nombre
