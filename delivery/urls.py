from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('clientes/', views.clientes, name='clientes'),
    path('pedidos/', views.pedidos, name='pedidos'),
     path('empleados/', views.empleados, name='empleados'),
    path('contabilidad/', views.contabilidad, name='contabilidad')
]