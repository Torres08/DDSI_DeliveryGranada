from django import forms
from .models import Usuario, Employee, Restaurante, Pedido, Ingreso, Gasto

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['Nombre', 'Apellidos', 'Telefono', 'Direccion', 'DNI']

class EliminaUsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['Nombre', 'Apellidos']  

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

class PedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = ['estado', 'fecha_creacion', 'precio_total']

class IngresoForm(forms.ModelForm):
    class Meta:
        model = Ingreso
        fields = ['Importe', 'Fecha', 'comentario']

class GastoForm(forms.ModelForm):
    class Meta:
        model = Gasto
        fields = ['Importe', 'Fecha', 'comentario']
