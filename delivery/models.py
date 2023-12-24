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

class Usuario(Cliente):
    DNI = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return f"{self.id} - {self.Nombre}"

class Menu(models.Model):
    nombre = models.CharField(max_length=100, null=True)


class Restaurante(Cliente):
    NRC = models.CharField(max_length=15, unique=True)
    Empleados = models.IntegerField()
    Propietario = models.CharField(max_length=40)
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return f"Restaurante {self.id} - {self.Nombre}"


# ----------------------------------------------------------------------------------------------------------------------
# Subsitema 2: Logistica
# definido: Producto, Pedido, encarga, comunica, asigna
class Producto(models.Model):
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=255)
    precio = models.DecimalField(max_digits=10, decimal_places=2)

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

    Estado = models.CharField(max_length=40, choices=ESTADO_CHOICES, default=EN_PREPARACION)
    productos = models.ManyToManyField('Producto', through='DetallePedido')
    precio_total = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    latitud = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    longitud = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    restaurante = models.ForeignKey(Restaurante, on_delete=models.CASCADE, default=1)  # Restaurante al que pertenece el pedido

    def __str__(self):
        return f"Pedido {self.id} - Estado: {self.Estado}"

    def calcular_precio_total(self):
        return sum(detalle.precio_total() for detalle in self.detallepedido_set.all())

    def cambiar_coordenadas(self):
        # Seleccionar aleatoriamente una de las coordenadas preestablecidas
        nueva_coordenada = random.choice(self.COORDENADAS_PREESTABLECIDAS)
        self.latitud, self.longitud = nueva_coordenada

    def save(self, *args, **kwargs):
        # Guardar el pedido antes de realizar otras operaciones
        super(Pedido, self).save(*args, **kwargs)

        # Calcular el precio total después de guardar el pedido
        self.precio_total = self.calcular_precio_total()

        # Cambiar las coordenadas cada 2 minutos
        threading.Timer(120, self.cambiar_coordenadas).start()

    def cambiar_estado_despues_de_3_minutos(self):
        # Cambiar estado a "En Reparto" después de 3 minutos
        if self.Estado == 'En Preparación':
            threading.Timer(180, self.cambiar_estado_a_en_reparto).start()

    def cambiar_estado_a_en_reparto(self):
        self.Estado = 'En Reparto'
        self.save()  # Guarda el estado actualizado
        # Cambiar estado a "Entregado" después de 5 minutos
        threading.Timer(300, self.cambiar_estado_a_entregado).start()

    def cambiar_estado_a_entregado(self):
        self.estado = 'Entregado'
        self.save()  # Guarda el estado actualizado


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

#@receiver(post_save, sender=DetallePedido)
#def recalcular_precio_total_pedido(sender, instance, **kwargs):
#    instance.pedido.precio_total = instance.pedido.calcular_precio_total()
#    instance.pedido.save()


class Encarga(models.Model):
    usuario = models.ForeignKey(Usuario, unique=True, on_delete=models.CASCADE)
    pedido = models.ForeignKey(Pedido, unique=True, on_delete=models.CASCADE)

# comunica no es necesario, ya que el pedido tiene un restaurante
#class Comunica(models.Model):
#    restaurante = models.ForeignKey(Restaurante, unique=True, on_delete=models.CASCADE)
#    pedido = models.ForeignKey(Pedido, unique=True, on_delete=models.CASCADE)


# ----------------------------------------------------------------------------------------------------------------------
# Subsitema 4: Contabilidad
# definido: Ingreso, Gasto, Produce, Emite
class Ingreso(models.Model):
    Importe = models.IntegerField()
    Fecha = models.DateTimeField()
    # Emisor = models.CharField(max_length=30)

class Gasto(models.Model):
    Importe = models.IntegerField()
    Fecha = models.DateTimeField()
    # Destinatario = models.CharField(max_length=30)


class Emite(models.Model):
    pedido = models.ForeignKey(Pedido, unique=True, null=True, on_delete=models.CASCADE)
    ingreso = models.ForeignKey(Ingreso, unique=True, on_delete=models.CASCADE)

# ----------------------------------------------------------------------------------------------------------------------
# Human Resources
# definido: Employee, Worktime, Schedule, Rating

class Employee(models.Model):
    Nombre = models.CharField(max_length=30, unique=True)
    Apellidos = models.CharField(max_length=30)
    Direccion = models.CharField(max_length=255)
    Telefono = models.CharField(max_length=9, null=True)
    Salario = models.DecimalField(max_digits=10, decimal_places=2)
    IBAN = models.CharField(max_length=25)
    Mail = models.CharField(max_length=30)
    Hire_date = models.DateField()

class Worktime(models.Model):
    worktime = models.DecimalField(max_digits=10, decimal_places=2)
    efficiency = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)])
    deliveries = models.IntegerField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()

class Schedule(models.Model):
    worktime = models.ForeignKey(Worktime, unique=True, null=True, on_delete=models.CASCADE)
    empleado = models.ForeignKey(Employee, unique=True, null=True, on_delete=models.CASCADE)

class Rating(models.Model):
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    empleado = models.ForeignKey(Employee, unique=True, null=True, on_delete=models.CASCADE)

class Asigna(models.Model):
    pedido = models.ForeignKey(Pedido, unique=True, on_delete=models.CASCADE)
    empleado = models.ForeignKey(Employee, unique=True, on_delete=models.CASCADE)

class Produce(models.Model):
    empleado = models.ForeignKey(Employee, unique=True, on_delete=models.CASCADE)
    gasto = models.ForeignKey(Gasto, unique=True, on_delete=models.CASCADE)





