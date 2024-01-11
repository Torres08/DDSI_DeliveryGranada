from django import forms
from .models import Cliente

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['Nombre', 'Telefono', 'Direccion']

class EliminaClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['Nombre']  

class ModificarClienteForm(forms.Form):
    Nombre = forms.CharField(max_length=255)
    NuevoNombre = forms.CharField(max_length=255)
    NuevoTelefono = forms.CharField(max_length=9)
    NuevaDireccion = forms.CharField(max_length=255)
