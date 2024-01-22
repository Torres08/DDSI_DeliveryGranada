from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render , get_object_or_404
from .models import *
from .forms import *
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.urls import reverse
from django.views.decorators.http import require_POST

def home(request):
   return render(request, "home.html")


# usuario 




def usuario(request):
    usuarios = Usuario.objects.all()
    return render(request, 'usuarios/usuarios.html', {'usuarios': usuarios})

from django.shortcuts import render, redirect
from .forms import UsuarioForm
from .models import Usuario

def crear_usuario(request):
    form = UsuarioForm(request.POST or None)
    
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('usuarios')
        else:
            print(form.errors)

    return render(request, 'usuarios/crearusuarios.html', {'form': form})

def eliminar_usuarios(request, id):
    usuario = get_object_or_404(Usuario, id=id)

    if request.method == 'POST':
        # Verifica si el usuario ha confirmado el borrado
        confirmacion = request.POST.get('confirmacion')
        if confirmacion == 'si':
            usuario.delete()
            return redirect('usuarios')

    return render(request, 'usuarios/eliminar_usuarios.html', {'usuario': usuario})

def modificar_usuario(request, id):
    usuario = get_object_or_404(Usuario, id=id)
    form = UsuarioForm(request.POST or None, instance=usuario)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('usuarios')
        else:
            print(form.errors)

    return render(request, 'usuarios/modificar_usuarios.html', {'form': form, 'usuario': usuario})

#############################################


def restaurante(request):
    restaurantes = Restaurante.objects.all()
    return render(request, 'restaurantes/restaurantes.html', {'restaurantes': restaurantes})

def crear_restaurante(request):

    form = RestauranteForm(request.POST or None)
    
    if form.is_valid():
        form.save()
        return redirect('restaurante')

    return render(request, 'restaurantes/crearrestaurantes.html', {'form' : form})

def eliminar_restaurante(request):
    return render(request, 'restaurantes/eliminarrestaurantes.html')

def modificar_restaurante(request):
    return render(request, 'restaurantes/modificarrestaurantes.html')

def pedidos(request):
    pedidos = Pedido.objects.all()
    return render(request, 'pedidos/pedidos.html',{'pedidos': pedidos})

def crear_pedido(request):
    return render(request, 'pedidos/crearpedidos.html')

def eliminar_pedido(request):
    return render(request, 'pedidos/eliminarpedidos.html')

def modificar_pedido(request):
    return render(request, 'pedidos/modificarpedidos.html')

def empleados(request):
    trabajadores = Employee.objects.all()
    return render(request, 'empleados/empleados.html', {'trabajadores': trabajadores})

def crear_empleado(request):
    form = EmpleadoForm(request.POST or None)
    
    if form.is_valid():
        form.save()
        return redirect('empleados')

    return render(request, 'empleados/crearempleados.html', {'form': form})

def eliminar_empleado(request):
    return render(request, 'empleados/eliminarempleados.html')

def modificar_empleado(request):
    return render(request, 'empleados/modificarempleados.html')

def contabilidad(request):
    return render(request, 'contabilidad/contabilidad.html')

def crear_contabilidad(request):
    return render(request, 'contabilidad/crearcontabilidad.html')

def eliminar_contabilidad(request):
    return render(request, 'contabilidad/eliminarcontabilidad.html')

def modificar_contabilidad(request):
    return render(request, 'contabilidad/modificarcontabilidad.html')

def ingresos(request):
    ingresos = Ingreso.objects.all()
    return render(request, 'contabilidad/ingreso/ingresos.html', {'ingresos': ingresos})

def crear_ingreso(request):
    form = IngresoForm(request.POST or None)
    
    if form.is_valid():
        form.save()
        return redirect('ingresos')
    return render(request, 'contabilidad/ingreso/crearingreso.html', {'form': form})

def eliminar_ingreso(request):
    return render(request, 'contabilidad/ingreso/eliminaringreso.html')

def modificar_ingreso(request):
    return render(request, 'contabilidad/ingreso/modificaringreso.html')

def gastos(request):
    gastos = Gasto.objects.all()
    return render(request, 'contabilidad/gasto/gastos.html',{'gastos': gastos})

def crear_gasto(request):
    form = GastoForm(request.POST or None)
    
    if form.is_valid():
        form.save()
        return redirect('gastos')
    return render(request, 'contabilidad/gasto/creargasto.html',{'form': form})

def eliminar_gasto(request):
    return render(request, 'contabilidad/gasto/eliminargasto.html')

def modificar_gasto(request):
    return render(request, 'contabilidad/gasto/modificargasto.html')

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

