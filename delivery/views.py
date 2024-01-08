from django.http import HttpResponse
from django.shortcuts import render
from .models import Usuario, Cliente
from .forms import ClienteForm
from django.shortcuts import render, redirect

def home(request):
   usuarios = Usuario.objects.all()
   return render(request, "home.html", {"usuarios": usuarios})



from django.http import JsonResponse

def clientes(request):
    if request.method == 'POST':
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

            return JsonResponse({'cliente': data_cliente})
        else:
            # Devolver errores del formulario
            return JsonResponse({'error': form.errors}, status=400)
    else:
        form = ClienteForm()

    clientes = Cliente.objects.all()
    return render(request, 'clientes.html', {'form': form, 'clientes': clientes})


def pedidos(request):
    return render(request, 'pedidos.html')

def empleados(request):
    return render(request, 'empleados.html')

def contabilidad(request):
    return render(request, 'contabilidad.html')



