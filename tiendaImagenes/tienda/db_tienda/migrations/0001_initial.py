# Generated by Django 3.2.5 on 2021-07-06 22:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Clientes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo_cliente', models.CharField(max_length=10)),
                ('empresa', models.CharField(max_length=50)),
                ('foto_cliente', models.ImageField(upload_to='upload/')),
                ('nombre_cliente', models.CharField(max_length=50)),
                ('apellido_cliente', models.CharField(max_length=50)),
                ('puesto', models.CharField(max_length=50)),
                ('direccion', models.CharField(max_length=100)),
                ('poblacion', models.CharField(max_length=100)),
                ('telefono', models.CharField(max_length=10)),
                ('cp', models.CharField(max_length=5)),
                ('cc', models.CharField(max_length=16)),
            ],
        ),
        migrations.CreateModel(
            name='Productos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo_producto', models.CharField(max_length=10)),
                ('foto_producto', models.ImageField(upload_to='upload/')),
                ('nombre_producto', models.CharField(max_length=50)),
                ('Descripcion_producto', models.CharField(max_length=100)),
                ('codigo_proveedor', models.CharField(max_length=10)),
                ('precio_unidad', models.CharField(max_length=10)),
                ('unidad_existencia', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Pedidos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo_pedido', models.CharField(max_length=10)),
                ('numero_pedido', models.CharField(max_length=10)),
                ('codigo_cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='db_tienda.clientes')),
                ('codigo_producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='db_tienda.productos')),
            ],
        ),
    ]
