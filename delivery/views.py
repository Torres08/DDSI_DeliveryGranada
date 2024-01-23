from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render , get_object_or_404
from .models import *
from .forms import *
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.urls import reverse

def home(request):
   return render(request, "home.html")

# usuario
def usuario(request):
    usuarios = Usuario.objects.all()
    return render(request, 'usuarios/usuarios.html', {'usuarios': usuarios})

def crear_usuario(request):
    form = UsuarioForm(request.POST or None)
    
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('usuarios')
        else:
            print(form.errors)

    return render(request, 'usuarios/crear_usuarios.html', {'form': form})

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

def eliminar_usuarios(request, id):
    usuario = get_object_or_404(Usuario, id=id)

    if request.method == 'POST':
        # Verifica si el usuario ha confirmado el borrado
        confirmacion = request.POST.get('confirmacion')
        if confirmacion == 'si':
            usuario.delete()
            return redirect('usuarios')

    return render(request, 'usuarios/eliminar_usuarios.html', {'usuario': usuario})

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

def eliminar_restaurantes(request):
    restaurante = get_object_or_404(Restaurante, id=id)

    if request.method == 'POST':
        # Verifica si el usuario ha confirmado el borrado
        confirmacion = request.POST.get('confirmacion')
        if confirmacion == 'si':
            restaurante.delete()
            return redirect('restaurantes')

    return render(request, 'restaurantes/eliminar_restaurantes.html', {'restaurantes': restaurante})

def modificar_restaurantes(request):
    restaurante = get_object_or_404(Restaurante, id=id)
    form = RestauranteForm(request.POST or None, instance=restaurante)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('restaurantes')
        else:
            print(form.errors)

    return render(request, 'restaurantes/modificar_restaurantes.html', {'form': form, 'restaurante': restaurante})

#############################################
# pedidos

def pedidos(request):
    pedidos = Pedido.objects.all()
    return render(request, 'pedidos/pedidos.html',{'pedidos': pedidos})

def crear_pedido(request):
    productos_cantidad_formset = None  # Inicializar la variable fuera del bloque condicional

    if request.method == 'POST':
        form = PedidoForm(request.POST)
        if form.is_valid():
            pedido = form.save()
            productos_cantidad_formset = ProductoCantidadFormSet(request.POST, instance=pedido, prefix='productos_cantidad')
            if productos_cantidad_formset.is_valid():
                productos_cantidad_formset.save()
                return redirect('pedidos')  # Reemplaza 'lista_pedidos' con el nombre de tu vista de lista de pedidos
    else:
        form = PedidoForm()

    return render(request, 'pedidos/crear_pedidos.html', {'form': form, 'productos_cantidad_formset': productos_cantidad_formset}) 

def eliminar_pedidos(request, id):
    pedido = get_object_or_404(Pedido, id=id)

    if request.method == 'POST':
        # Verifica si el usuario ha confirmado el borrado
        confirmacion = request.POST.get('confirmacion')
        if confirmacion == 'si':
            pedido.delete()
            return redirect('pedidos')

    return render(request, 'pedidos/eliminar_pedidos.html', {'pedidos': pedido})

def modificar_pedido(request, id):
    pedidos = get_object_or_404(Pedido, id=id)
    form = PedidoForm(request.POST or None, instance=pedidos)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('pedidos')
        else:
            print(form.errors)

    return render(request, 'pedidos/modificar_pedidos.html', {'form': form, 'pedidos': pedidos})

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

    return render(request, 'empleados/modificar_empleados.html', {'form': form, 'empleados': empleados})

#############################################

#contabilidad

def contabilidad(request):
    return render(request, 'contabilidad/contabilidad.html')

# ingreso

def ingresos(request):
    ingresos = Ingreso.objects.all()
    return render(request, 'contabilidad/ingreso/ingresos.html', {'ingresos': ingresos})

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

    return render(request, 'contabilidad/ingreso/eliminar_ingreso.html', {'ingresos': ingreso})

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

# gasto

def gastos(request):
    gastos = Gasto.objects.all()
    return render(request, 'contabilidad/gasto/gastos.html',{'gastos': gastos})

def crear_gasto(request):
    form = GastoForm(request.POST or None)
    
    if form.is_valid():
        form.save()
        return redirect('gastos')
    return render(request, 'contabilidad/gasto/crear_gasto.html',{'form': form})

def eliminar_gasto(request, id):
    gasto = get_object_or_404(Gasto, id=id)

    if request.method == 'POST':
        # Verifica si el usuario ha confirmado el borrado
        confirmacion = request.POST.get('confirmacion')
        if confirmacion == 'si':
            gasto.delete()
            return redirect('gastos')

    return render(request, 'contabilidad/gasto/eliminar_gasto.html', {'gastos': gasto})

def modificar_gasto(request, id):
    gasto = get_object_or_404(Gasto, id=id)
    form = GastoForm(request.POST or None, instance=gasto)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('gastos')
        else:
            print(form.errors)

    return render(request, 'contabilidad/gasto/modificar_gastos.html', {'form': form, 'gastos': gasto})

#####################################################


#menu
def menu(request, restaurante_id):
    menu = Menu.objects.filter(restaurante_id=restaurante_id)
    return render(request, 'restaurantes/menu/menu.html',{'menu': menu})

def crear_menu(request):
    if request.method == 'POST':
        form = MenuForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('menu')
    else:
        form = MenuForm()

    restaurantes = Restaurante.objects.all()

    return render(request, 'restaurantes/menu/crear_menu.html', {'form': form, 'restaurantes': restaurantes})

def eliminar_menu(request, menu_id):
    menu = get_object_or_404(Menu, id=menu_id)

    if request.method == 'POST':
        # Verifica si el usuario ha confirmado el borrado
        confirmacion = request.POST.get('confirmacion')
        if confirmacion == 'si':
            menu.delete()
            return redirect('detalle_menu')

    return render(request, 'restaurantes/menu/eliminar_menu.html', {'menu': menu})


def detalle_menu(request, menu_id):
    menu = get_object_or_404(Menu, id=menu_id)
    productos = menu.producto_set.all()  # 'producto_set' es el nombre por defecto para la relación inversa

    return render(request, 'restaurantes/menu/detalle_menu.html', {'menu': menu, 'productos': productos})

#producto

def añadir_producto(request, restaurante_id):
    restaurante = Restaurante.objects.get(id=restaurante_id)

    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            producto = form.save(commit=False)
            producto.restaurante = restaurante
            producto.save()
            return redirect('menu', restaurante_id=restaurante_id)
    else:
        form = ProductoForm()

    return render(request, 'restaurantes/menu/añadir_producto.html', {'form': form, 'restaurante': restaurante})


def eliminar_producto(request, id):
    producto = get_object_or_404(Producto, id=id)

    if request.method == 'POST':
        # Verifica si el usuario ha confirmado el borrado
        confirmacion = request.POST.get('confirmacion')
        if confirmacion == 'si':
            restaurante_id = producto.restaurante.id
            producto.delete()

            return redirect('menu', restaurante_id=restaurante_id)

    return render(request, 'restaurantes/menu/eliminar_producto.html', {'productos': producto})

def modificar_producto(request, id):
    producto = get_object_or_404(Producto, id=id)
    form = ProductoForm(request.POST or None, instance=producto)

    if request.method == 'POST':
        if form.is_valid():
            form.save()

            restaurante_id = producto.restaurante.id

            return redirect('menu', restaurante_id=restaurante_id)
        else:
            print(form.errors)

    return render(request, 'restaurantes/menu/modificar_producto.html', {'form': form, 'productos': producto})
