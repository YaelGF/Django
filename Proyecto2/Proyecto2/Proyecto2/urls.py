"""Proyecto2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from basics.views import saludar, adios, dameFecha, saludoSimple, saludoParametros, saludoShortcut
from basics.views import saludoLoader, carrera_tics, carrera_Alimentos
from basics.views import CalcularEdad
from basics.views import calcularEdad_V1, calcularEdad_V2,calcularEdad_V3

urlpatterns = [
    path('admin/', admin.site.urls),
    path('saludar/',saludar),
    path('despedida/', adios),
    path('fecha/', dameFecha),
    path('calcular/<int:anio>/<int:edad>', CalcularEdad),
    path('saludo1', saludoSimple),
    path('saludo2', saludoParametros),
    path('saludo3', saludoShortcut),
    path('saludo4', saludoLoader),
    path('tics', carrera_tics),
    path('alimentos', carrera_Alimentos),
    path('caso1/<int:day>/<int:month>/<int:year>/<int:yearS>', calcularEdad_V1),
    path('caso2/<int:year>/<int:yearS>', calcularEdad_V2),
    path('caso3/<int:day>/<int:month>/<int:year>/<int:yearS>', calcularEdad_V3),
]
