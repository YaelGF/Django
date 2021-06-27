from django.shortcuts import redirect, render
from .forms import Clientes_form, Pedido_form, Productos_form
from .models import Clientes,Pedidos,Productos

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

def form_productos(request, id=0):
    if request.method == "GET":
        if id == 0:
            form=Productos_form()
        else:
            producto = Productos.objects.get(pk=id)
            form = Productos_form(instance = producto)
        return render(request,'productos/form_productos.html',{'form': form})
    else:
        if(id == 0):
            form = Productos_form(request.POST)
        else:
            producto = Productos.objects.get(pk=id)
            form = Productos_form(request.POST, instance = producto)
        if(form.is_valid()):
            form.save()
        return redirect('/tienda/listar_productos/')

def form_clientes(request, id=0):
    if request.method == "GET":
        if id == 0:
            form=Clientes_form()
        else:
            cliente = Clientes.objects.get(pk=id)
            form = Clientes_form(instance = cliente)
        return render(request,'clientes/form_clientes.html',{'form': form})
    else:
        if(id == 0):
            form = Clientes_form(request.POST)
        else:
            cliente = Clientes.objects.get(pk=id)
            form = Clientes_form(request.POST, instance = cliente)
        if(form.is_valid()):
            form.save()
        return redirect('/tienda/listar_clientes/')

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