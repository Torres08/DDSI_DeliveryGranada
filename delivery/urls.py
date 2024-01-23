from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('usuarios/', views.usuario, name='usuarios'),
    path('usuarios/crear_usuario', views.crear_usuario, name='crear_usuarios'),
    path('usuarios/<int:id>/eliminar_usuarios/', views.eliminar_usuarios, name='eliminar_usuarios'),
    path('usuarios/<int:id>/modificar_usuarios/', views.modificar_usuario, name='modificar_usuarios'),

    
    path('restaurantes/', views.restaurante, name='restaurantes'),
    path('restaurantes/crear_restaurante', views.crear_restaurante, name='crear_restaurantes'),
    path('restaurantes/<int:id>/eliminar_restaurantes/', views.eliminar_restaurantes, name='eliminar_restaurantes'),
    path('restaurantes/<int:id>/modificar_restaurantes/', views.modificar_restaurantes, name='modificar_restaurantes'),

    path('empleados/', views.empleados, name='empleados'),
    path('empleados/crear_empleado', views.crear_empleado, name='crear_empleados'),
    path('empleados/<int:id>/eliminar_empleados/', views.eliminar_empleados, name='eliminar_empleados'),
    path('empleados/<int:id>/modificar_empleados/', views.modificar_empleados, name='modificar_empleados'),

    path('contabilidad/', views.contabilidad, name='contabilidad'),

    path('contabilidad/ingresos', views.ingresos, name='ingresos'),
    path('contabilidad/ingresos/crear_ingreso', views.crear_ingreso, name='crear_ingresos'),
    path('contabilidad/ingresos/<int:id>/eliminar_ingresos/', views.eliminar_ingreso, name='eliminar_ingresos'),
    path('contabilidad/ingresos/<int:id>/modificar_ingresos/', views.modificar_ingreso, name='modificar_ingresos'),

    path('contabilidad/gastos', views.gastos, name='gastos'),
    path('contabilidad/crear_gasto', views.crear_gasto, name='crear_gastos'),
    path('contabilidad/eliminar_gasto', views.eliminar_gasto, name='eliminar_gastos'),
    path('contabilidad/modificar_gasto', views.modificar_gasto, name='modificar_gastos'),

    #path('contabilidad/eliminar_ingreso', views.eliminar_ingreso, name='eliminar_ingresos'),
    #path('contabilidad/modificar_ingreso', views.modificar_ingreso, name='modificar_ingresos'),

    #path('empleados/eliminar_empleado', views.eliminar_empleado, name='eliminar_empleados'),
    #path('empleados/modificar_empleado', views.modificar_empleado, name='modificar_empleados'),
    
   
    path('pedidos/', views.pedidos, name='pedidos'),
    path('pedidos/crear_pedido', views.crear_pedido, name='crear_pedidos'),
    path('pedidos/<int:id>/eliminar_pedido', views.eliminar_pedidos, name='eliminar_pedidos'),
    path('pedidos/<int:id>/modificar_pedido', views.modificar_pedido, name='modificar_pedidos'),
    
    path('restaurantes/<int:restaurante_id>/menu/', views.menu, name='menu'),
    path('menu/crear/', views.crear_menu, name='crear_menu'),
    path('menu/<int:menu_id>/eliminar_menu/', views.eliminar_menu, name='eliminar_menu'),
    path('menu/<int:id>/detalle_menu', views.detalle_menu, name='detalle_menu'),
    path('menu/añadir_producto/', views.añadir_producto, name='añadir_producto'),
    path('menu/<int:id>/eliminar_producto/', views.eliminar_producto, name='eliminar_producto'),
    path('menu/<int:id>/modificar_producto/', views.modificar_producto, name='modificar_producto'),
]