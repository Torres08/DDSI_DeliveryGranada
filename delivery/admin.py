from django.contrib import admin
from django import forms

# Register your models here.
from .models import Pedido, Encarga, Cliente, Usuario, Restaurante, Menu, Producto, Employee, Worktime, Rating, Asigna, Ingreso, Gasto, Produce, Emite, Comunica, Schedule, DetallePedido # Importa tu modelo

# admin.site.register(Pedido)
admin.site.register(DetallePedido)
admin.site.register(Encarga)
admin.site.register(Cliente)
admin.site.register(Usuario)
admin.site.register(Restaurante)
admin.site.register(Employee)
admin.site.register(Worktime)
admin.site.register(Rating)
admin.site.register(Asigna)
admin.site.register(Ingreso)
admin.site.register(Gasto)
admin.site.register(Produce)
admin.site.register(Emite)
admin.site.register(Comunica)
admin.site.register(Schedule)

class PedidoAdmin(admin.ModelAdmin):
    exclude = ['latitud', 'longitud', 'Estado']

admin.site.register(Pedido, PedidoAdmin)



class ProductoInline(admin.TabularInline):
    model = Producto
    extra = 1

class MenuAdmin(admin.ModelAdmin):
    inlines = [ProductoInline]

#admin.site.register(Restaurante)
admin.site.register(Menu, MenuAdmin)
admin.site.register(Producto)








