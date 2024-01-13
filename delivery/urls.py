from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('clientes/', views.clientes, name='clientes'),
    path('pedidos/', views.pedidos, name='pedidos'),
    path('pedidos/crear_pedido', views.crear_pedido, name='crear_pedidos'),
    path('pedidos/eliminar_pedido', views.eliminar_pedido, name='eliminar_pedidos'),
    path('pedidos/modificar_pedido', views.modificar_pedido, name='modificar_pedidos'),
    path('empleados/', views.empleados, name='empleados'),
    path('contabilidad/', views.contabilidad, name='contabilidad')
]