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

    #
    path('empleados/ver_rating_worktime/<int:empleado_id>/', views.ver_rating_worktime, name='ver_rating_worktime'),

    path('contabilidad/ingresos', views.ingresos, name='ingresos'),
    path('contabilidad/ingresos/crear_ingreso', views.crear_ingreso, name='crear_ingresos'),
    path('contabilidad/ingresos/<int:id>/eliminar_ingresos/', views.eliminar_ingreso, name='eliminar_ingresos'),
    path('contabilidad/ingresos/<int:id>/modificar_ingresos/', views.modificar_ingreso, name='modificar_ingresos'),

    #path('contabilidad/eliminar_ingreso', views.eliminar_ingreso, name='eliminar_ingresos'),
    #path('contabilidad/modificar_ingreso', views.modificar_ingreso, name='modificar_ingresos'),

    #path('empleados/eliminar_empleado', views.eliminar_empleado, name='eliminar_empleados'),
    #path('empleados/modificar_empleado', views.modificar_empleado, name='modificar_empleados'),
    
   
    path('pedidos/', views.pedidos, name='pedidos'),
    path('pedidos/crear_pedido', views.crear_pedido, name='crear_pedidos'),
    path('pedidos/eliminar_pedido', views.eliminar_pedido, name='eliminar_pedidos'),
    path('pedidos/modificar_pedido', views.modificar_pedido, name='modificar_pedidos'),
    
    path('contabilidad/', views.contabilidad, name='contabilidad'),
    path('contabilidad/crear_contabilidad', views.crear_contabilidad, name='crear_contabilidad'),
    path('contabilidad/eliminar_contabilidad', views.eliminar_contabilidad, name='eliminar_contabilidad'),
    path('contabilidad/modificar_contabilidad', views.modificar_contabilidad, name='modificar_contabilidad'),
    
    path('contabilidad/gastos', views.gastos, name='gastos'),
    path('contabilidad/crear_gasto', views.crear_gasto, name='crear_gastos'),
    path('contabilidad/gastos/<int:id>/eliminar_gastos/', views.eliminar_gasto, name='eliminar_gastos'),
    path('contabilidad/gastos/<int:id>/modificar_gastos/', views.modificar_gasto, name='modificar_gastos'),
    
    path('clientes/', views.clientes, name='clientes'),
    
    path('restaurantes/<int:id>/menu/', views.ver_menu_restaurante, name='ver_menu_restaurante')

    
]