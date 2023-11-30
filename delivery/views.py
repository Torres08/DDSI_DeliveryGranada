from django.http import HttpResponse
from .models import Pedido  # Asegúrate de reemplazar con el nombre real de tu modelo

def index(request):
    # Obtén todos los objetos de la clase Pedido
    pedidos = Pedido.objects.all()

    # Construye una cadena con los contenidos de los pedidos
    pedidos_str = "\n".join([f"Pedido {pedido.id}: {pedido.Nombre_Productos}" for pedido in pedidos])

    # Crea una respuesta HTTP con la cadena de pedidos
    response = HttpResponse(f"Listado de Pedidos:\n{pedidos_str}")

    return response