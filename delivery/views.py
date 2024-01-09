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
            print ("adios")
            form = ClienteForm(request.POST)
            print("hola")
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

    clientes = Cliente.objects.all()
    return render(request, 'clientes.html', {'form': form, 'clientes': clientes})



def pedidos(request):
    return render(request, 'pedidos.html')

def empleados(request):
    return render(request, 'empleados.html')

def contabilidad(request):
    return render(request, 'contabilidad.html')



