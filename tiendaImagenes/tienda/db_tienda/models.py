from django.db import models

# Create your models here.
class Clientes(models.Model):
    codigo_cliente = models.CharField(max_length=10,blank=True)
    empresa = models.CharField(max_length=50,blank=True)
    foto_cliente = models.ImageField(upload_to = 'upload/',blank = True)
    nombre_cliente = models.CharField(max_length=50,blank=True)
    apellido_cliente = models.CharField(max_length=50,blank=True)
    puesto = models.CharField(max_length=50,blank=True)
    direccion = models.CharField(max_length=100,blank=True)
    poblacion = models.CharField(max_length=100,blank=True)
    telefono = models.CharField(max_length=10,blank=True)
    cp = models.CharField(max_length=5,blank=True)
    cc = models.CharField(max_length=16,blank=True)
    #INSERT INTO db_tienda_app_clientes (codigo_cliente,empresa,nombre_cliente,apellido_cliente,puesto,direccion,poblacion,telefono,cp,numerocc) VALUES (1,'Bimbo','Arturo','Perez','Vendedor','Tulancingo','Tulancingo',7751159586,43650,1234567891123456);
    def __str__(self):
        return self.nombre_cliente

class Productos(models.Model):
    codigo_producto = models.CharField(max_length=10,blank=True)
    foto_producto = models.ImageField(upload_to = 'upload/',blank=True)
    nombre_producto = models.CharField(max_length=50,blank=True)
    Descripcion_producto = models.CharField(max_length=100,blank=True)
    codigo_proveedor = models.CharField(max_length=10,blank=True)
    precio_unidad = models.CharField(max_length=10,blank=True)
    unidad_existencia = models.CharField(max_length=10,blank=True)
    #INSERT INTO db_tienda_app_productos (codigo_producto,nombre_producto,descripcion_producto,codigo_proveedor,precio_unidad,unidad_existencia) VALUES (1,'Coca-cola','Refresco reducido en azucar',141516,20,500);
    def __str__(self):
        return self.nombre_producto

class Pedidos(models.Model):
    codigo_pedido = models.CharField(max_length=10)
    numero_pedido = models.CharField(max_length=10)
    codigo_cliente = models.ForeignKey(Clientes,on_delete=models.CASCADE)
    codigo_producto = models.ForeignKey(Productos,on_delete=models.CASCADE)