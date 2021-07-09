from django.shortcuts import redirect, render
from django.urls.base import is_valid_path
from .forms import Clientes_form, Pedido_form, Productos_form
from .models import Clientes,Pedidos,Productos
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView
from django.urls import reverse_lazy

# Create your views here.


def listar_productos(request, id=0):
    context = {'listar_productos' : Productos.objects.all()}
    return render(request,'productos/listar_productos.html',context)

def listar_pedidos(request, id=0):
    context = {'listar_pedidos' : Pedidos.objects.all()}
    return render(request,'pedidos/listar_pedidos.html',context)

def listar_clientes(request, id=0):
    context = {'listar_clientes' : Clientes.objects.all()}
    return render(request,'clientes/listar_clientes.html',context)

def form_pedidos(request, id=0):
    if request.method == "GET":
        if id == 0:
            form=Pedido_form()
        else:
            pedido = Pedidos.objects.get(pk=id)
            form = Pedido_form(instance = pedido)
        return render(request,'pedidos/form_pedidos.html',{'form': form})
    else:
        if(id == 0):
            form = Pedido_form(request.POST)
        else:
            pedido = Pedidos.objects.get(pk=id)
            form = Pedido_form(request.POST, instance = pedido)
        if(form.is_valid()):
            form.save()
        return redirect('/tienda/listar_pedidos/')

def borrar_pedidos(request, id):
    pedido = Pedidos.objects.get(pk=id)
    pedido.delete()
    return  redirect('/tienda/listar_pedidos/')

def borrar_productos(request, id):
    producto = Productos.objects.get(pk=id)
    producto.delete()
    return  redirect('/tienda/listar_productos/')

def borrar_clientes(request, id):
    cliente = Clientes.objects.get(pk=id)
    cliente.delete()
    return  redirect('/tienda/listar_clientes/')

class ProductosImage(TemplateView):
    template_name = 'productos/form_productos.html'

    def post (self, request,id=0):
        if(id == 0):
            form = Productos_form(request.POST, request.FILES)
        else:
            producto = Productos.objects.get(pk=id)
            form = Productos_form(request.POST, request.FILES, instance = producto)
        if (form.is_valid()):
            form.save()
            return redirect ('/tienda/listar_productos/')
        context = self.get_context_data(form = form)
        return self.render_to_response(context)

    def get(self, request,id=0):
        if id == 0:
            return self.post(request,id)
        else:
            producto = Productos.objects.get(pk=id)
            form = Productos_form( instance = producto)
        return render(request,'productos/form_productos.html',{'form': form})

class ClientesImage(TemplateView):
    form = Clientes_form
    template_name = 'clientes/form_clientes.html'
    def post (self, request,id=0):
        if(id == 0):
            form = Clientes_form(request.POST, request.FILES)
        else:
            cliente = Clientes.objects.get(pk=id)
            form = Clientes_form(request.POST, request.FILES, instance = cliente)
        if form.is_valid():
            form.save()
            return redirect('/tienda/listar_clientes/')
        context = self.get_context_data(form = form)
        return  self.render_to_response(context)   

    def get(self, request,id=0):
        if id == 0:
            return self.post(request,id)
        else:
            cliente = Clientes.objects.get(pk=id)
            form = Clientes_form( instance = cliente)
            return render(request,'clientes/form_clientes.html',{'form': form})
        