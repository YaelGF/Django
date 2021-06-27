from django.db import models

# Create your models here.

class Grupo(models.Model):
    title = models.CharField(max_length=50)
    def __str__(self):
        return self.title 

class alumno(models.Model):
    nombre = models.CharField(max_length=50)
    apellido_paterno = models.CharField(max_length=50)
    apellido_materno = models.CharField(max_length=50)
    no_control = models.CharField(max_length=10)
    cuatrimestre = models.CharField(max_length=5)
    grupo = models.ForeignKey(Grupo, on_delete=models.CASCADE)

