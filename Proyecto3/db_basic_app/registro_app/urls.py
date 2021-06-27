from django.urls import path,include
from .import views

urlpatterns = [
    path('',views.form_alumnos, name="insert_alumnos"),
    path('<int:id>/',views.form_alumnos, name='update_registros'),
    path('eliminar/<int:id>/',views.borrar_alumnos, name='delete_registro'),
    path('listar_alumnos/',views.listar_alumnos, name='lista_alumnos'),
]
