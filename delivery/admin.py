from django.contrib import admin
from django import forms
from django.core.validators import MinValueValidator, MaxValueValidator

from .models import *  # Import your models

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
# admin.site.register(Emite)
admin.site.register(Schedule)

class ProductoInline(admin.TabularInline):
    model = Producto
    extra = 1

class MenuAdmin(admin.ModelAdmin):
    inlines = [ProductoInline]

admin.site.register(Menu, MenuAdmin)
admin.site.register(Producto)


class DetallePedidoForm(forms.ModelForm):
    class Meta:
        model = DetallePedido
        fields = '__all__'

class DetallePedidoInline(admin.TabularInline):
    model = DetallePedido
    form = DetallePedidoForm
    extra = 0  # Puedes ajustar la cantidad de formularios en línea que deseas mostrar

class PedidoAdmin(admin.ModelAdmin):
    exclude = ['latitud', 'longitud', 'Estado','precio_total']
    inlines = [DetallePedidoInline]

admin.site.register(Pedido, PedidoAdmin)








