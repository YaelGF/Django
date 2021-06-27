from django import forms
from django.db import models
from django.forms import fields
from .models import alumno

class Alumno_form(forms.ModelForm):
    class Meta:
        model = alumno
        fields = ('nombre','apellido_paterno','apellido_materno','no_control','cuatrimestre','grupo') 
        labels = {
            'no_control':'Numero de Control',
            'apellido_paterno':'Apellido Paterno',
            'apellido_materno':'Apellido Materno'
            }
        
    def __init__(self,*args,**kwargs):
        super(Alumno_form,self).__init__(*args,**kwargs)
        self.fields['grupo'].empty_label = "Elige un grupo"
        self.fields['apellido_materno'].required = False
