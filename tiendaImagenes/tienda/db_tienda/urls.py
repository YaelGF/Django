from django.urls import path, include
from . import views
from .views import ClientesImage, ProductosImage

urlpatterns = [
    path('', views.form_pedidos, name='insert_pedido'),
    path('<int:id>/', views.form_pedidos, name='update_pedidos'),
    path('listar_pedidos/', views.listar_pedidos, name='listar_pedidos'),
    path('eliminar/<int:id>/', views.borrar_pedidos, name='delete_pedidos'),

    path('form_clientes', ClientesImage.as_view(), name='insert_cliente'),
    path('editar_clientes/<int:id>/',ClientesImage.as_view(), name='update_clientes'),
    path('listar_clientes/', views.listar_clientes, name='listar_clientes'),
    path('eliminar_clientes/<int:id>/', views.borrar_clientes, name='delete_clientes'),
    
    path('form_productos/',ProductosImage.as_view(), name='insert_producto'),
    path('editar_productos/<int:id>/',ProductosImage.as_view(), name='update_productos'),
    path('listar_productos/', views.listar_productos, name='listar_productos'),
    path('eliminar_productos/<int:id>/', views.borrar_productos, name='delete_productos'),

]


