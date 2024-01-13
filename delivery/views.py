from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render , get_object_or_404
from .models import *
from .forms import *
from django.shortcuts import render, redirect
from django.http import JsonResponse

def home(request):
   return render(request, "home.html")


def usuario(request):
    return render(request, 'usuarios/usuarios.html')

def crear_usuario(request):

    form = UsuarioForm(request.POST or None)
    
    if form.is_valid():

        form.save()

    return render(request, 'usuarios/crearusuarios.html', {'form' : form})

def modificar_usuario(request, id):
    
    # Obtener el objeto Usuario o devolver 404 si no existe
    usuario = get_object_or_404(Usuario, id=id)

    if request.method == 'POST':
        # Rellenar el formulario con los datos del POST y la instancia actual
        form = UsuarioForm(request.POST, instance=usuario)

        if form.is_valid():
            # Guardar los cambios y redirigir a la vista de detalle
            form.save()
            return HttpResponseRedirect("/"+str(id))
    else:
        # Crear el formulario con la instancia actual
        form = UsuarioForm(instance=usuario)
    
    return render(request, 'usuarios/modificarusuarios.html', {'form': form, 'usuario': usuario})

def eliminar_usuario(request):
    form = EliminaUsuarioForm()

    if request.method == 'POST':
        # Resto del código para eliminar cliente...

        return render(request, 'clientes/eliminar_cliente.html', {'form': form})
    
    return render(request, 'usuarios/eliminarusuarios.html', {'form': form})

def listar_usuarios(request):
    usuarios = Usuario.objects.all()
    return render(request, 'usuarios/usuarios.html', {'usuarios': usuarios})

def restaurante(request):
    return render(request, 'restaurantes/restaurantes.html')

def crear_restaurante(request):

    form = RestauranteForm(request.POST or None)
    
    if form.is_valid():

        form.save()

    return render(request, 'restaurantes/crearrestaurantes.html', {'form' : form})

def eliminar_restaurante(request):
    return render(request, 'restaurantes/eliminarrestaurantes.html')

def modificar_restaurante(request):
    return render(request, 'restaurantes/modificarrestaurantes.html')

def pedidos(request):
    return render(request, 'pedidos/pedidos.html')

def crear_pedido(request):
    return render(request, 'pedidos/crearpedidos.html')

def eliminar_pedido(request):
    return render(request, 'pedidos/eliminarpedidos.html')

def modificar_pedido(request):
    return render(request, 'pedidos/modificarpedidos.html')

def empleados(request):
    return render(request, 'empleados/empleados.html')

def crear_empleado(request):
    form = EmpleadoForm(request.POST or None)
    
    if form.is_valid():

        form.save()

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


