import random
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.dispatch import receiver
from django.utils import timezone
import threading

# py manage.py makemigrations
# py manage.py migrate 
# py manage.py runserver

# ----------------------------------------------------------------------------------------------------------------------
# Subsitema 1: Cliente
# definido: Cliente, Usuario, Menu, Restaurante
class Cliente(models.Model):
    Nombre = models.CharField(max_length=255)
    Telefono = models.CharField(max_length=9)
    Direccion = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.id} - {self.Nombre}"
    
    def eliminar_cliente(self):
        # Método para eliminar el cliente
        self.delete()

class Usuario(Cliente):
    DNI = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return f"{self.id} - {self.Nombre}"

class Restaurante(Cliente):
    NRC = models.CharField(max_length=15, unique=True)
    Empleados = models.IntegerField()
    Propietario = models.CharField(max_length=40)

    def __str__(self):
        return f"Restaurante {self.id} - {self.Nombre}"

class Menu(models.Model):
    restaurante = models.ForeignKey(Restaurante, on_delete=models.CASCADE, null=True, related_name='menus')

# ----------------------------------------------------------------------------------------------------------------------
# Subsitema 4: Contabilidad
# definido: Ingreso, Gasto, Produce, Emite
class Ingreso(models.Model):
    Importe = models.IntegerField()
    Fecha = models.DateTimeField()

class Gasto(models.Model):
    Importe = models.IntegerField()
    Fecha = models.DateTimeField()

# ----------------------------------------------------------------------------------------------------------------------
# Human Resources
# definido: Employee, Worktime, Schedule, Rating

class Rating(models.Model):
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    comentario = models.TextField(blank=True, null=True)  
    empleado = models.ForeignKey('Employee', related_name='ratings',null=True, on_delete=models.CASCADE)
    

class Worktime(models.Model):
    efficiency = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)])
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    
class Employee(models.Model):
    Nombre = models.CharField(max_length=30, unique=True)
    Direccion = models.CharField(max_length=255)
    Telefono = models.CharField(max_length=9, null=True)
    Salario = models.DecimalField(max_digits=10, decimal_places=2)
    IBAN = models.CharField(max_length=25)
    Mail = models.CharField(max_length=30)
    #Hire_date = models.DateField()
    
    # un empleado tiene un worktime, un schedule y un rating
    worktime = models.OneToOneField(Worktime,null=True, on_delete=models.CASCADE)
    gasto = models.OneToOneField(Gasto, null=True, on_delete=models.CASCADE)
    
     # añadir varios ratings a un empleado
    def add_rating(self, rating_value, comentario=None):
        rating = Rating.objects.create(empleado=self, rating=rating_value, comentario=comentario)
        return rating


# ----------------------------------------------------------------------------------------------------------------------
# Subsitema 2: Logistica
# definido: Producto, Pedido, encarga, comunica, asigna
class Producto(models.Model):
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(null=True)
    precio = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return f"{self.nombre} - ${self.precio}"

class Pedido(models.Model):
    EN_PREPARACION = 'En Preparación'
    EN_ENVIO = 'En Envío'
    ENTREGADO = 'Entregado'

    ESTADO_CHOICES = [
        (EN_PREPARACION, 'En Preparación'),
        (EN_ENVIO, 'En Envío'),
        (ENTREGADO, 'Entregado'),
    ]

    COORDENADAS_PREESTABLECIDAS = [  # pasarlo a una API si eso
        (40.7128, -74.0060),  # punto 1
        (34.0522, -118.2437),  # punto 2
        (41.8781, -87.6298),  # punto 3
        (37.7749, -122.4194),  # punto 4
        (51.5074, -0.1278),  # punto 5
    ]

    estado = models.CharField(max_length=40, choices=ESTADO_CHOICES, default=EN_PREPARACION)
    fecha_creacion = models.DateTimeField(default=timezone.now)
    precio_total = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    latitud = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    longitud = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    restaurante = models.ForeignKey(Restaurante, on_delete=models.CASCADE, default=1)
    productos = models.ManyToManyField('Producto', through='DetallePedido', limit_choices_to={'menu__restaurante': Restaurante})
    
    gasto_generado = models.OneToOneField(Gasto, null=True, blank=True, on_delete=models.SET_NULL, related_name='pedidos_asignados')
    empleado_asignado = models.ForeignKey(Employee, null=True, blank=True, on_delete=models.SET_NULL, related_name='pedidos_asignados')
    usuario_asignado = models.ForeignKey(Usuario, null=True, blank=True, on_delete=models.SET_NULL, related_name='pedidos_asignados')

    def __str__(self):
        return f"Pedido {self.id} - Estado: {self.estado}"

    def calcular_precio_total(self):
        detalles = self.detallepedido_set.all()
        print (sum(detalle.producto.precio * detalle.cantidad for detalle in detalles))
        return  sum(detalle.producto.precio * detalle.cantidad for detalle in detalles)
        
    def save(self, *args, **kwargs):
        # Calcular el precio total antes de guardar el pedido
        self.precio_total = self.calcular_precio_total()

        # Establecer la fecha de creación solo si no está establecida previamente
        if not self.fecha_creacion:
            self.fecha_creacion = timezone.now()

        # Guardar el pedido con el precio total actualizado y la fecha de creación
        super(Pedido, self).save(*args, **kwargs)

        # Cambiar las coordenadas cada 2 minutos
        threading.Timer(120, self.cambiar_coordenadas).start()

    def cambiar_coordenadas(self):
        # Seleccionar aleatoriamente una de las coordenadas preestablecidas
        nueva_coordenada = random.choice(self.COORDENADAS_PREESTABLECIDAS)
        self.latitud, self.longitud = nueva_coordenada
    
# relacion entre producto y pedido con info adicional
class DetallePedido(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(default=1,validators=[MinValueValidator(1), MaxValueValidator(20)])   
    
    class Meta:
        #Garantiza que no se pueda repetir el mismo producto en un pedido
        unique_together = ('pedido', 'producto')
     
    def precio_total(self):
        return self.producto.precio * self.cantidad















