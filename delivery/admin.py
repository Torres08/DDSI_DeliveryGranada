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



class DetallePedidoInline(admin.TabularInline):
    model = DetallePedido
    extra = 0

class PedidoAdmin(admin.ModelAdmin):
    exclude = [ 'Estado', 'precio_total']
    inlines = [DetallePedidoInline]

    def save_related(self, request, form, formsets, change):
        # Override save_related to ensure the Pedido instance is saved first
        super().save_related(request, form, formsets, change)
        form.instance.save()

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

class WorktimeForm(forms.ModelForm):
    class Meta:
        model = Worktime
        fields = '__all__'

    def clean_efficiency(self):
        efficiency = self.cleaned_data['efficiency']
        if not (0 <= efficiency <= 5):
            raise forms.ValidationError('La eficiencia debe estar entre 0 y 5.')
        return efficiency

class WorktimeInline(admin.TabularInline):
    model = Worktime
    form = WorktimeForm
    extra = 1

class EmployeeAdmin(admin.ModelAdmin):
    inlines = [RatingInline, WorktimeInline]

admin.site.register(Employee, EmployeeAdmin)


# añadir varios worktine a empleado








