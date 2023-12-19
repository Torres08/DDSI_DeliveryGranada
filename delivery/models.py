from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.dispatch import receiver
from django.db.models.signals import post_save, post_delete
from django.utils import timezone
import threading
from datetime import timedelta

# Cliente

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

class Restaurante(Cliente):
    NRC = models.CharField(max_length=15, unique=True)
    Empleados = models.IntegerField()
    Propietario = models.CharField(max_length=40)
        
    def __str__(self):
         return f"{self.id} - {self.Nombre}"

class Menu(models.Model):
    restaurante = models.OneToOneField(Restaurante, on_delete=models.CASCADE)

class Producto(models.Model):
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=255)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
        
    def __str__(self):
        return f"{self.nombre} - ${self.precio}"

# Human Resources
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
    
# Logistica
    
#class Producto(models.Model):
 #   Nombre_Producto = models.CharField(max_length=100,null=True)
  #  Cantidad = models.IntegerField(null=True)

   # def __str__(self):
    #    return self.Nombre_Producto

class Pedido(models.Model):
        
    EN_PREPARACION = 'En Preparación'
    EN_ENVIO = 'En Envío'
    ENTREGADO = 'Entregado'

    ESTADO_CHOICES = [
        (EN_PREPARACION, 'En Preparación'),
        (EN_ENVIO, 'En Envío'),
        (ENTREGADO, 'Entregado'),
    ]

    Estado = models.CharField(max_length=40, choices=ESTADO_CHOICES, default=EN_PREPARACION)
    productos = models.ManyToManyField(Producto, through='DetallePedido')
    precio_total = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)

    def __str__(self):
        return f"Pedido {self.id} - Estado: {self.Estado}"

    def calcular_precio_total(self):
        return sum(detalle.precio_total() for detalle in self.detallepedido_set.all())

    def save(self, *args, **kwargs):
        # Calcular el precio total antes de guardar el pedido
        self.precio_total = self.calcular_precio_total()
        super(Pedido, self).save(*args, **kwargs)

    def cambiar_estado_despues_de_3_minutos(self):
        # Cambiar estado a "En Reparto" después de 3 minutos
        if self.estado == 'En Preparación':
            threading.Timer(180, self.cambiar_estado_a_en_reparto).start()

    def cambiar_estado_a_en_reparto(self):
        self.estado = 'En Reparto'
        self.save()
        # Cambiar estado a "Entregado" después de 5 minutos
        threading.Timer(300, self.cambiar_estado_a_entregado).start()

    def cambiar_estado_a_entregado(self):
        self.estado = 'Entregado'
        self.save()

class DetallePedido(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(default=0)

    def precio_total(self):
        return self.producto.precio * self.cantidad

class Encarga(models.Model):
    usuario = models.ForeignKey(Usuario, unique=True, on_delete=models.CASCADE)
    pedido = models.ForeignKey(Pedido, unique=True, on_delete=models.CASCADE)

class Comunica(models.Model):
    restaurante = models.ForeignKey(Restaurante, unique=True, on_delete=models.CASCADE)
    pedido = models.ForeignKey(Pedido, unique=True, on_delete=models.CASCADE)

class Asigna(models.Model):
    pedido = models.ForeignKey(Pedido, unique=True, on_delete=models.CASCADE)
    empleado = models.ForeignKey(Employee, unique=True, on_delete=models.CASCADE)

# Contabilidad

class Ingreso(models.Model):
    Importe = models.IntegerField()
    Fecha = models.DateTimeField()
    #Emisor = models.CharField(max_length=30)

class Gasto(models.Model):
    Importe = models.IntegerField()
    Fecha = models.DateTimeField()
    #Destinatario = models.CharField(max_length=30)

class Produce(models.Model):
    empleado = models.ForeignKey(Employee, unique=True, on_delete=models.CASCADE)
    gasto = models.ForeignKey(Gasto, unique=True, on_delete=models.CASCADE)

class Emite(models.Model):
    pedido = models.ForeignKey(Pedido, unique=True, null=True, on_delete=models.CASCADE)
    ingreso = models.ForeignKey(Ingreso, unique=True, on_delete=models.CASCADE)




