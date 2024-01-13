from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('usuarios/', views.usuario, name='usuarios'),
    path('usuarios/crear_usuario', views.crear_usuario, name='crear_usuarios'),
    path('usuarios/eliminar_usuario', views.eliminar_usuario, name='eliminar_usuarios'),
    path('usuarios/modificar_usuario', views.modificar_usuario, name='modificar_usuarios'),
    path('usuarios/listar_usuario', views.listar_usuarios, name='listar_usuarios'),
    path('restaurantes/', views.restaurante, name='restaurantes'),
    path('restaurantes/crear_restaurante', views.crear_restaurante, name='crear_restaurantes'),
    path('restaurantes/eliminar_restaurante', views.eliminar_restaurante, name='eliminar_restaurantes'),
    path('restaurantes/modificar_restaurante', views.modificar_restaurante, name='modificar_restaurantes'),
    path('pedidos/', views.pedidos, name='pedidos'),
    path('pedidos/crear_pedido', views.crear_pedido, name='crear_pedidos'),
    path('pedidos/eliminar_pedido', views.eliminar_pedido, name='eliminar_pedidos'),
    path('pedidos/modificar_pedido', views.modificar_pedido, name='modificar_pedidos'),
    path('empleados/', views.empleados, name='empleados'),
    path('empleados/crear_empleado', views.crear_empleado, name='crear_empleados'),
    path('empleados/eliminar_empleado', views.eliminar_empleado, name='eliminar_empleados'),
    path('empleados/modificar_empleado', views.modificar_empleado, name='modificar_empleados'),
    path('contabilidad/', views.contabilidad, name='contabilidad'),
    path('contabilidad/crear_contabilidad', views.crear_contabilidad, name='crear_contabilidad'),
    path('contabilidad/eliminar_contabilidad', views.eliminar_contabilidad, name='eliminar_contabilidad'),
    path('contabilidad/modificar_contabilidad', views.modificar_contabilidad, name='modificar_contabilidad'),
]