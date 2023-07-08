from django.urls import path 
from . import views 

# /<str:pk> es el parametro

urlpatterns = [
    path('index', views.index , name='index'),
    path('listaProductos', views.listaProductos, name='listaProductos'),
    path('agregarProductos', views.agregarProductos, name='agregarProductos'),
    path('editarProductos/<str:pk>', views.editarProductos, name='editarProductos'),
    path('eliminarProductos/<str:pk>', views.eliminarProductos, name='eliminarProductos'),
    path('registrarUsuario', views.registrarUsuario, name='registrarUsuario'),
    path('ingresoUsuario', views.ingresoUsuario, name='ingresoUsuario'),
    path('contactoGeneral', views.contactoGeneral, name='contactoGeneral'),
]