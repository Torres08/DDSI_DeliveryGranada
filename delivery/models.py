import random
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.dispatch import receiver
from django.utils import timezone
import threading
from django.db.models.signals import post_save

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
        return f"Cliente: {self.Nombre} - {self.id}"
    
    def eliminar_cliente(self):
        # Método para eliminar el cliente
        self.delete()


class Usuario(Cliente):
    Apellidos = models.CharField(max_length=255, null=True)
    DNI = models.CharField(max_length=9 , unique=True)

    def __str__(self):
        return f"Usuario: {self.Nombre} - {self.id}"


class Restaurante(Cliente):
    NRC = models.CharField(max_length=15, unique=True)
    Empleados = models.IntegerField()
    Propietario = models.CharField(max_length=40)

    def __str__(self):
        return f"Restaurante {self.Nombre} - {self.id}"

class Menu(models.Model):
    restaurante = models.ForeignKey(Restaurante, on_delete=models.CASCADE, null=True, related_name='menus')
    
    @property
    def menu_name(self):
        if self.restaurante:
            return f"Menu {self.restaurante.Nombre}"
        else:
            return "Menu (No Restaurant)"

    def __str__(self):
        return self.menu_name

# ----------------------------------------------------------------------------------------------------------------------
# Human Resources
# definido: Employee, Worktime, Schedule, Rating

class Rating(models.Model):
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    comentario = models.TextField(blank=True, null=True)  
    empleado = models.ForeignKey('Employee', related_name='ratings',null=True, on_delete=models.CASCADE)
    
    @property
    def menu_name(self):
        if self.empleado:
            return f"Rating Empleado: {self.empleado.Nombre}"
        else:
            return "Rating Empleado: (No Employee selected)"

    def __str__(self):
        return self.menu_name
    
class Worktime(models.Model):
    efficiency = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)])
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    employee = models.ForeignKey('Employee', related_name='worktimes', null=True, on_delete=models.CASCADE)
    
    @property
    def menu_name(self):
        if self.employee:
            return f"Worktime Empleado: {self.employee.Nombre}"
        else:
            return "Worktime Empleado: (No Employee selected)"

    def __str__(self):
        return self.menu_name

    
class Employee(models.Model):
    Nombre = models.CharField(max_length=30)
    Apellidos = models.CharField(max_length=30)
    Direccion = models.CharField(max_length=255)
    Telefono = models.CharField(max_length=9, null=True)
    IBAN = models.CharField(max_length=25, unique=True)
    Mail = models.CharField(max_length=30)
    disponible = models.BooleanField(default=True)
    
    def __str__(self):
        return f"{self.Nombre} - ID:{self.pk}"
    
     # añadir varios ratings a un empleado
    def add_rating(self, rating_value, comentario=None):
        rating = Rating.objects.create(empleado=self, rating=rating_value, comentario=comentario)
        return rating
    
    def add_worktime(self, efficiency, start_date, end_date):
        worktime = Worktime.objects.create(employee=self, efficiency=efficiency, start_date=start_date, end_date=end_date)
        return worktime


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

    ESTADO_CHOICES = (
        ('En Preparación', 'En preparación'),
        ('envio', 'En envío'),
        ('entregado', 'Entregado'),
    )

    estado = models.CharField(max_length=40, choices=ESTADO_CHOICES, default='En Preparación')
    fecha_creacion = models.DateTimeField(default=timezone.now)
    precio_total = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    #latitud = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    #longitud = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    restaurante = models.ForeignKey(Restaurante, on_delete=models.CASCADE, default=1)
    productos = models.ManyToManyField('Producto', through='DetallePedido', limit_choices_to={'menu__restaurante': Restaurante})
    repartidor = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True, blank=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"Pedido {self.id} - Estado: {self.estado}"

    def calcular_precio_total(self):
        detalles = self.detallepedido_set.all()
        print (sum(detalle.producto.precio * detalle.cantidad for detalle in detalles))
        return  sum(detalle.producto.precio * detalle.cantidad for detalle in detalles)
        
    #def save(self, *args, **kwargs):
        # Calcular el precio total antes de guardar el pedido
        #self.precio_total = self.calcular_precio_total()

        # Guardar el pedido con el precio total actualizado y la fecha de creación
        #super(Pedido, self).save(*args, **kwargs)

        # Cambiar las coordenadas cada 2 minutos
        #threading.Timer(120, self.cambiar_coordenadas).start()

    ##def cambiar_coordenadas(self):
        # Seleccionar aleatoriamente una de las coordenadas preestablecidas
        ##nueva_coordenada = random.choice(self.COORDENADAS_PREESTABLECIDAS)
        ##self.latitud, self.longitud = nueva_coordenada

    
class Asigna(models.Model):

    trabajador = models.ForeignKey(Employee, on_delete=models.CASCADE)
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('trabajador', 'pedido')  # Garantiza que un pedido solo pueda asignarse a un trabajador una vez

# Actualización del receptor para asignar automáticamente un trabajador al crear un pedido
@receiver(post_save, sender=Pedido)
def asignar_repartidor(sender, instance, created, **kwargs):
    if created and instance.estado == 'En preparación' and Employee.objects.filter(disponible=True).exists():
        repartidor_disponible = Employee.objects.filter(disponible=True).first()
        instance.repartidor = repartidor_disponible
        instance.save()
        repartidor_disponible.disponible = False
        repartidor_disponible.save()

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


class Encarga(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('usuario', 'pedido')

# ----------------------------------------------------------------------------------------------------------------------
# Subsitema 4: Contabilidad
# definido: Ingreso, Gasto, Produce, Emite
class Ingreso(models.Model):
    Importe = models.IntegerField()
    Fecha = models.DateTimeField()
    comentario = models.TextField(blank=True, null=True)
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE, null=True)

    class Meta:
        unique_together = ('pedido',)  # Garantiza que solo haya un ingreso por pedido   

class Gasto(models.Model):
    Importe = models.IntegerField()
    Fecha = models.DateTimeField()
    comentario = models.TextField(blank=True, null=True)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, null=True)





