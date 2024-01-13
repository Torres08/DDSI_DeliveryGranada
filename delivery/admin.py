from django.contrib import admin
from django import forms
from django.core.validators import MinValueValidator, MaxValueValidator

from .models import Pedido, Cliente, Usuario, Restaurante, Menu, Producto, Employee, Worktime, Rating, Ingreso, Gasto, DetallePedido  # Import your models

admin.site.register(Cliente)
admin.site.register(Usuario)
admin.site.register(Restaurante)
#admin.site.register(Employee)
admin.site.register(Worktime)
admin.site.register(Rating)
admin.site.register(Ingreso)
admin.site.register(Gasto)


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

    def __init__(self, *args, **kwargs):
        # Llamamos al método __init__ del formulario base
        super().__init__(*args, **kwargs)

        # Obtener la instancia del pedido si existe
        pedido_instance = kwargs.get('instance', None)

        # Filtrar los productos por el restaurante del pedido
        if pedido_instance and pedido_instance.pk:
            restaurante = pedido_instance.restaurante
            self.fields['producto'].queryset = self.fields['producto'].queryset.filter(menu__restaurante=restaurante)

class DetallePedidoInline(admin.TabularInline):
    model = DetallePedido
    form = DetallePedidoForm
    extra = 0  # Puedes ajustar la cantidad de formularios en línea que deseas mostrar

class PedidoAdmin(admin.ModelAdmin):
    exclude = ['latitud', 'longitud', 'Estado','precio_total']
    inlines = [DetallePedidoInline]

admin.site.register(Pedido, PedidoAdmin)


# añadir varios rating a empleado
class RatingForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = '__all__'

    def clean_rating(self):
        rating = self.cleaned_data['rating']
        if not (1 <= rating <= 5):
            raise forms.ValidationError('El rating debe estar entre 1 y 5.')
        return rating

class RatingInline(admin.TabularInline):
    model = Rating
    form = RatingForm
    extra = 1

class EmployeeAdmin(admin.ModelAdmin):
    inlines = [RatingInline]

admin.site.register(Employee, EmployeeAdmin)






