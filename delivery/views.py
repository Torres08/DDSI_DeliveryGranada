from django.http import HttpResponse
from django.shortcuts import render
from .models import Usuario, Cliente
from .forms import *
from django.shortcuts import render, redirect
from django.http import JsonResponse


def home(request):
   usuarios = Usuario.objects.all()
   return render(request, "home.html", {"usuarios": usuarios})


def clientes(request):
    form = ClienteForm()  # Mueve la definición de form aquí

    if request.method == 'POST':
        accion = request.POST.get('accion')
        if accion == 'crear':
            form = ClienteForm(request.POST)
            if form.is_valid():
                nuevo_cliente = form.save()

                # Devolver los datos del cliente como JSON
                data_cliente = {
                    'id': nuevo_cliente.id,
                    'nombre': nuevo_cliente.Nombre,
                    'telefono': nuevo_cliente.Telefono,
                    'direccion': nuevo_cliente.Direccion,
                }
                print(data_cliente)
                
                return JsonResponse({'cliente': data_cliente})
            else:
                # Devolver errores del formulario
                return JsonResponse({'error': form.errors}, status=400)
            
        elif accion == 'eliminar':
            form = EliminaClienteForm(request.POST)
            print(form.data)
            if form.is_valid():

                nombre_cliente = form.cleaned_data['Nombre']

                # Eliminar el cliente
                Cliente.objects.get(Nombre=nombre_cliente).delete()
                
                return JsonResponse({'eliminado': True})
                
            else:
                # Devolver errores del formulario
                return JsonResponse({'error': form.errors}, status=400)
        
        elif accion == 'modificar':
            form = ModificarClienteForm(request.POST)
            print(form.data)
            
            if form.is_valid():
            
                nombre_cliente = form.cleaned_data['Nombre']
                print(nombre_cliente)
                # Aquí debes identificar el cliente que deseas modificar
                try:
                    cliente_a_modificar = Cliente.objects.get(Nombre=nombre_cliente)
                except Cliente.DoesNotExist:
                    return JsonResponse({'error': 'El cliente no existe'}, status=400)

                # Actualiza los atributos del cliente con los nuevos valores del formulario
                cliente_a_modificar.Nombre = form.cleaned_data['NuevoNombre']  # Ajusta según tu formulario
                cliente_a_modificar.Telefono = form.cleaned_data['NuevoTelefono']
                cliente_a_modificar.Direccion = form.cleaned_data['NuevaDireccion']
                
                # Guarda los cambios en la base de datos
                cliente_a_modificar.save()

                # Devuelve una respuesta JSON indicando que se ha modificado el cliente
                return JsonResponse({'modificado': True})
            else:
                # Devuelve errores del formulario si no es válido
                print(form.errors)
                return JsonResponse({'error': form.errors}, status=400)

    clientes = Cliente.objects.all()
# views.py
    lista_clientes = [{'id': cliente.id, 'Nombre': cliente.Nombre, 'telefono': cliente.Telefono, 'direccion': cliente.Direccion} for cliente in clientes]
        
    return render(request, 'clientes.html', {'form': form, 'clientes': clientes, 'lista_clientes': lista_clientes})


def pedidos(request):
    return render(request, 'pedidos.html')

def empleados(request):
    return render(request, 'empleados.html')

def contabilidad(request):
    return render(request, 'contabilidad.html')



