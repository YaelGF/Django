from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template, Context, loader

import datetime

def saludar(request):

    return HttpResponse("Hola, estamos usando una respuesta directa")

def adios (request):

    return HttpResponse("Esto es todo amiguitos")

def dameFecha(request):

    ahora = datetime.datetime.now()

    msg = f'Estamos tomando clases el {ahora}'

    return HttpResponse(msg)

def CalcularEdad(request, anio, edad):

    edadActual = edad
    now = datetime.datetime.now().year

    print(now)

    periodo = anio - now

    edadPosterior = edadActual + periodo

    message = f'en el año {anio} tendras {edadPosterior}'

    return HttpResponse(message)

def saludoSimple(request):

    paginaSaludo = open('/home/yael/Develoment/Python-Django/Proyecto2/Proyecto2/basics/templates/views/saludo_dinamico.html')

    plt =  Template(paginaSaludo.read())

    paginaSaludo.close()

    ctx = Context()

    docPagSaludo = plt.render(ctx)

    return HttpResponse(docPagSaludo)

class estudiante(object):

    def __init__(self,nombre, apellido):

        self.nombre = nombre
        self.apellido = apellido

def saludoParametros(request):

    paginaSaludo = open('/home/yael/Develoment/Python-Django/Proyecto2/Proyecto2/basics/templates/views/parametros.html')

    estudiante1 = estudiante("Margarita", "Perez Sosa")

    arreglo_2 = ["valor_1","valor_2","valor_3"]

    arreglo_3 = ["0","1","2","3","4","5","6","7","8","9","10"]

    ahora = datetime.datetime.now()

    plt =  Template(paginaSaludo.read())

    paginaSaludo.close()

    ctx = Context({"nombre_estudiante" : estudiante1.nombre, "apellido_estudiante" : estudiante1.apellido,"arreglo_1":["Elemento1","Elemento2"],"arreglo_2" : arreglo_2, "arreglo_3" : arreglo_3,"fecha": ahora})

    docPagSaludo = plt.render(ctx)

    return HttpResponse(docPagSaludo)

def saludoShortcut(request):

    estudiante1 = estudiante("Alicia", "Perez Sosa")

    arreglo_2 = ["valor_1","valor_2","valor_3"]

    arreglo_3 = ["0","1","2","3","4","5","6","7","8","9","10"]

    ahora = datetime.datetime.now()

    return render(request, "parametros.html",{"nombre_estudiante" : estudiante1.nombre, "apellido_estudiante" : estudiante1.apellido,"arreglo_1":["Elemento1","Elemento2"],"arreglo_2" : arreglo_2, "arreglo_3" : arreglo_3,"fecha": ahora})

#Loader

def saludoLoader(request):

    paginaSaludo = open('/home/yael/Develoment/Python-Django/Proyecto2/Proyecto2/basics/templates/views/parametros.html')

    estudiante1 = estudiante("Margarita", "La Diosa de La cumbia!!!!")

    arreglo_2 = ["valor_1","valor_2","valor_3"]

    arreglo_3 = ["0","1","2","3","4","5","6","7","8","9","10"]

    ahora = datetime.datetime.now()

    paginaLoader = loader.get_template("parametros.html")

    docPagSaludo = paginaLoader.render({"nombre_estudiante" : estudiante1.nombre, "apellido_estudiante" : estudiante1.apellido,"arreglo_1":["Elemento1","Elemento2"],"arreglo_2" : arreglo_2, "arreglo_3" : arreglo_3,"fecha": ahora})

    return HttpResponse(docPagSaludo)

#Herencia

def carrera_tics(request):

    telefono_tics = "7751148510"

    return render(request,"Child1.html", {"telefono_tics": telefono_tics})

def carrera_Alimentos(request):

    telefono_alimentos = "775 854 81 96"

    return render(request,"Child2.html", {"telefono_alimentos" : telefono_alimentos})


def calcularEdad_V1(request,day, month,year,yearS):

    edad = yearS - year

    if (month > datetime.datetime.now().month):

        edad -= 1

    elif (month == datetime.datetime.now().month):

        if(day > datetime.datetime.now().day):

            edad -= 1
    
    message = f'Suponiendo que estamos en el {datetime.datetime.now().day}/{datetime.datetime.now().month}/{yearS} tendrias la edad de  {edad} años'

    return HttpResponse(message)

def calcularEdad_V2(request, year, yearS):

    edad = yearS - year

    message = f'En el año {yearS} tendras la edad de {edad} años'

    return HttpResponse(message)

def calcularEdad_V3(request,day, month, year, yearS):

    edad = yearS - year

    message = f'En el año {yearS} antes de la fecha {day}/{month} tendras la edad de {edad-1} años, pero despues de esa fecha, tendras la edad de {edad}'

    return HttpResponse(message)
    
# Create your views here.
