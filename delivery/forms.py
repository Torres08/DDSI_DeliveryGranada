from django import forms
from .models import Usuario, Employee, Restaurante, Pedido, Ingreso, Gasto, Producto, Menu, DetallePedido
from django.forms import formset_factory, inlineformset_factory

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['Nombre', 'Apellidos', 'Telefono', 'Direccion', 'DNI']

class EliminaUsuarioForm(forms.Form):
    usuario = forms.ModelChoiceField(queryset=Usuario.objects.all(), empty_label=None, to_field_name='id', label='Selecciona un usuario') 

class ModificarUsuarioForm(forms.Form):
    Nombre = forms.CharField(max_length=255)
    NuevoNombre = forms.CharField(max_length=255)
    NuevoApellidos = forms.CharField(max_length=255)
    NuevoTelefono = forms.CharField(max_length=9)
    NuevaDireccion = forms.CharField(max_length=255)
    NuevoDNI = forms.CharField(max_length=9)

class RestauranteForm(forms.ModelForm):
    class Meta:
        model = Restaurante
        fields = ['Nombre', 'Telefono', 'Direccion', 'NRC', 'Empleados', 'Propietario']

class EmpleadoForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['Nombre', 'Apellidos', 'Direccion', 'Telefono', 'IBAN', 'Mail', 'disponible']

#class DetallePedidoForm(forms.ModelForm):
#    class Meta:
#        model = DetallePedido
#        fields = ['producto', 'cantidad']

class DetallePedidoForm(forms.ModelForm):
    class Meta:
        model = DetallePedido
        fields = ['producto', 'cantidad']

ProductoCantidadFormSet = inlineformset_factory(Pedido, DetallePedido, form=DetallePedidoForm, extra=1)

class PedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = ['estado', 'fecha_creacion', 'usuario']

    productos_cantidad = ProductoCantidadFormSet(instance=Pedido(), prefix='productos_cantidad')   

class IngresoForm(forms.ModelForm):
    class Meta:
        model = Ingreso
        fields = ['Importe', 'Fecha', 'comentario', 'pedido']
        widgets = {
            'Fecha': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }

class GastoForm(forms.ModelForm):
    class Meta:
        model = Gasto
        fields = ['Importe', 'Fecha', 'comentario']

class MenuForm(forms.ModelForm):
    class Meta:
        model = Menu
        fields = ['restaurante']

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'descripcion', 'precio', 'menu']

