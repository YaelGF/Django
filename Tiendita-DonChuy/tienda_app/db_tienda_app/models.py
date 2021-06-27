from django.db import models

# Create your models here.

class Clientes(models.Model):
    codigo_cliente = models.CharField(max_length=10)
    empresa = models.CharField(max_length=50)
    nombre_cliente = models.CharField(max_length=50)
    apellido_cliente = models.CharField(max_length=50)
    puesto = models.CharField(max_length=50)
    direccion = models.CharField(max_length=100)
    poblacion = models.CharField(max_length=100)
    telefono = models.CharField(max_length=10)
    cp = models.CharField(max_length=5)
    numerocc = models.CharField(max_length=20)
    #INSERT INTO db_tienda_app_clientes (codigo_cliente,empresa,nombre_cliente,apellido_cliente,puesto,direccion,poblacion,telefono,cp,numerocc) VALUES (1,'Bimbo','Arturo','Perez','Vendedor','Tulancingo','Tulancingo',7751159586,43650,1234567891123456);
    def __str__(self):
        return self.nombre_cliente

class Productos(models.Model):
    codigo_producto = models.CharField(max_length=10)
    nombre_producto = models.CharField(max_length=50)
    Descripcion_producto = models.CharField(max_length=100)
    codigo_proveedor = models.CharField(max_length=10)
    precio_unidad = models.CharField(max_length=10)
    unidad_existencia = models.CharField(max_length=10)
    #INSERT INTO db_tienda_app_productos (codigo_producto,nombre_producto,descripcion_producto,codigo_proveedor,precio_unidad,unidad_existencia) VALUES (1,'Coca-cola','Refresco reducido en azucar',141516,20,500);
    def __str__(self):
        return self.nombre_producto

class Pedidos(models.Model):
    codigo_pedido = models.CharField(max_length=10)
    numero_pedido = models.CharField(max_length=10)
    codigo_cliente = models.ForeignKey(Clientes,on_delete=models.CASCADE)
    codigo_producto = models.ForeignKey(Productos,on_delete=models.CASCADE)