from django import forms
from django.db import models
from django.forms import fields
from .models import Pedidos,Clientes,Productos

class Pedido_form(forms.ModelForm):
    class Meta:
        model = Pedidos
        fields = ('codigo_pedido','numero_pedido','codigo_cliente','codigo_producto')
        labels= {'codigo_pedido': 'Codigo Pedido',
        'numero_pedido':'Numero Pedido',
        'codigo_cliente':'Codigo Cliente',
        'codigo_producto':'Codigo Producto'}
    
    def __init__(self,*args, **kwargs):
        super(Pedido_form,self).__init__(*args,**kwargs)
        self.fields['codigo_cliente'].empty_label = "Elige Cliente"
        self.fields['codigo_producto'].empty_label = "Elige Producto"

class Clientes_form(forms.ModelForm):
    class Meta:
        model = Clientes
        fields = ('codigo_cliente','empresa','nombre_cliente','apellido_cliente','puesto','direccion','poblacion','telefono','cp','numerocc')
        labels={'codigo_cliente':'Codigo Cliente',
        'nombre_cliente':'Nombre Cliente',
        'apellido_cliente':'Apellido Cliente',
        'numerocc':'CC'}

class Productos_form(forms.ModelForm):
    class Meta:
        model = Productos
        fields = ('codigo_producto','nombre_producto','Descripcion_producto','codigo_proveedor','precio_unidad','unidad_existencia')

