from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render , get_object_or_404
from .models import *
from .forms import *
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.urls import reverse
from django.views.decorators.http import require_POST
from django.db.models import Sum

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

# restaurante
def restaurante(request):
    restaurantes = Restaurante.objects.all()
    return render(request, 'restaurantes/restaurantes.html', {'restaurantes': restaurantes})

def crear_restaurante(request):
    form = RestauranteForm(request.POST or None)
    
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('restaurantes')
        else:
            print(form.errors)

    return render(request, 'restaurantes/crear_restaurantes.html', {'form': form})

def eliminar_restaurantes(request,id):
    restaurante = get_object_or_404(Restaurante, id=id)

    if request.method == 'POST':
        # Verifica si el usuario ha confirmado el borrado
        confirmacion = request.POST.get('confirmacion')
        if confirmacion == 'si':
            restaurante.delete()
            return redirect('restaurantes')

    return render(request, 'restaurantes/eliminar_restaurantes.html', {'restaurantes': restaurante})

def modificar_restaurantes(request, id):
    restaurante = get_object_or_404(Restaurante, id=id)
    form = RestauranteForm(request.POST or None, instance=restaurante)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('restaurantes')
        else:
            print(form.errors)

    return render(request, 'restaurantes/modificar_restaurantes.html', {'form': form, 'restaurante': restaurante})

def ver_menu_restaurante(request, id):
    # Obtener el restaurante por su ID o mostrar una página de error 404 si no se encuentra
    restaurante = get_object_or_404(Restaurante, id=id)

    # Obtener todos los productos asociados a este restaurante
    productos = Producto.objects.filter(menu__restaurante=restaurante)

    return render(request, 'restaurantes/menu.html', {'restaurante': restaurante, 'productos': productos})


#############################################
# empleados 

def empleados(request):
    trabajadores = Employee.objects.all()
    return render(request, 'empleados/empleados.html', {'trabajadores': trabajadores})

def crear_empleado(request):
    form = EmpleadoForm(request.POST or None)
    
    if form.is_valid():
        form.save()
        return redirect('empleados')

    return render(request, 'empleados/crear_empleados.html', {'form': form})

def eliminar_empleados(request, id):
    empleado = get_object_or_404(Employee, id=id)

    if request.method == 'POST':
        # Verifica si el usuario ha confirmado el borrado
        confirmacion = request.POST.get('confirmacion')
        if confirmacion == 'si':
            empleado.delete()
            return redirect('empleados')

    return render(request, 'empleados/eliminar_empleados.html', {'empleados': empleado})

def modificar_empleados(request,id):
    empleados = get_object_or_404(Employee, id=id)
    form = EmpleadoForm(request.POST or None, instance=empleados)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('empleados')
        else:
            print(form.errors)

    return render(request, 'empleados/modificar_empleados.html', {'form': form, 'empleado': empleados})

def ver_rating_worktime(request, empleado_id):
    empleado = get_object_or_404(Employee, id=empleado_id)
    ratings = Rating.objects.filter(empleado=empleado)
    worktimes = Worktime.objects.filter(employee=empleado)

    return render(request, 'empleados/ver_rating_worktime.html', {'empleado': empleado, 'ratings': ratings, 'worktimes': worktimes})

#############################################

# ingreso

def ingresos(request):
    ingresos = Ingreso.objects.all()
    gastos = Gasto.objects.all()

    hola_mundo = "¡Hola, Mundo!"
    total_ingresos = ingresos.aggregate(Sum('Importe'))['Importe__sum'] or 0  # Calcula la suma de los importes
    total_gastos = gastos.aggregate(Sum('Importe'))['Importe__sum'] or 0  # Calcula la suma de los importes
    
    balance = total_ingresos - total_gastos
    
    return render(request, 'contabilidad/ingreso/ingresos.html', {'total_gastos': total_gastos, 'ingresos': ingresos, 'hola_mundo': hola_mundo, 'total_ingresos': total_ingresos, 'balance': balance})

def crear_ingreso(request):
    form = IngresoForm(request.POST or None)
    
    if form.is_valid():
        form.save()
        return redirect('ingresos')
    return render(request, 'contabilidad/ingreso/crear_ingreso.html', {'form': form})

def eliminar_ingreso(request,id):
    ingreso = get_object_or_404(Ingreso, id=id)

    if request.method == 'POST':
        # Verifica si el usuario ha confirmado el borrado
        confirmacion = request.POST.get('confirmacion')
        if confirmacion == 'si':
            ingreso.delete()
            return redirect('ingresos')

    return render(request, 'contabilidad/ingreso/eliminar_ingresos.html', {'ingresos': ingreso})

def modificar_ingreso(request,id):
    ingreso = get_object_or_404(Ingreso, id=id)
    form = IngresoForm(request.POST or None, instance=ingreso)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('ingresos')
        else:
            print(form.errors)

    return render(request, 'contabilidad/ingreso/modificar_ingresos.html', {'form': form, 'ingresos': ingreso})

def gastos(request):
    gastos = Gasto.objects.all()
    ingresos = Ingreso.objects.all()

    total_ingresos = ingresos.aggregate(Sum('Importe'))['Importe__sum'] or 0  # Calcula la suma de los importes
    total_gastos = gastos.aggregate(Sum('Importe'))['Importe__sum'] or 0  # Calcula la suma de los importes
    
    balance = total_ingresos - total_gastos
    return render(request, 'contabilidad/gasto/gastos.html',{'gastos': gastos,'total_ingresos': total_ingresos, 'total_gastos': total_gastos, 'balance': balance})

def crear_gasto(request):
    form = GastoForm(request.POST or None)
    
    if form.is_valid():
        form.save()
        return redirect('gastos')
    return render(request, 'contabilidad/gasto/creargasto.html',{'form': form})

def eliminar_gasto(request,id):
    gasto = get_object_or_404(Gasto, id=id)

    if request.method == 'POST':
        # Verifica si el usuario ha confirmado el borrado
        confirmacion = request.POST.get('confirmacion')
        if confirmacion == 'si':
            gasto.delete()
            return redirect('gastos')

    return render(request, 'contabilidad/gasto/eliminar_gastos.html', {'gastos': gasto})


def modificar_gasto(request,id):
    gasto = get_object_or_404(Gasto, id=id)
    form = GastoForm(request.POST or None, instance=gasto)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('gastos')
        else:
            print(form.errors)

    return render(request, 'contabilidad/gasto/modificar_gastos.html', {'form': form, 'gastos': gasto})



#############################################

def pedidos(request):
    pedidos = Pedido.objects.all()

    for pedido in pedidos:
        detalles_pedido = DetallePedido.objects.filter(pedido=pedido)
        total_price = sum(detalle.precio_total() for detalle in detalles_pedido)
        pedido.total_price = total_price
    
    return render(request, 'pedidos/pedidos.html', {'pedidos': pedidos})

def crear_pedido(request):
    return render(request, 'pedidos/crearpedidos.html')

def eliminar_pedido(request):
    return render(request, 'pedidos/eliminarpedidos.html')

def modificar_pedido(request):
    return render(request, 'pedidos/modificarpedidos.html')


def contabilidad(request):
    return render(request, 'contabilidad/contabilidad.html')

def crear_contabilidad(request):
    return render(request, 'contabilidad/crearcontabilidad.html')

def eliminar_contabilidad(request):
    return render(request, 'contabilidad/eliminarcontabilidad.html')

def modificar_contabilidad(request):
    return render(request, 'contabilidad/modificarcontabilidad.html')
