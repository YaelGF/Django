from django import forms
from django.db import models
from django.forms import fields
from .models import Empleado

class EmpleadoForm(forms.ModelForm):
    class Meta:
        model = Empleado
        fields = ('nombre', 'emp_image')