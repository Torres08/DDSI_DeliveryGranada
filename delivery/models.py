from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
# Create your models here.
#Aquí se crean las tablas de la base de datos del sistema



# Cliente

class Cliente(models.Model):
    Nombre = models.CharField(max_length=255)
    Telefono = models.CharField(max_length=9)
    Direccion = models.CharField(max_length=255)

class Usuario(Cliente):
    DNI = models.CharField(max_length=20)

class Restaurante(Cliente):
    NRC = models.CharField(max_length=15)
    Empleados = models.IntegerField()
    Propietario = models.CharField(max_length=15)


# Human Resources
class Employee(models.Model):
    Nombre = models.CharField(max_length=30)
    Apellidos = models.CharField(max_length=30)
    Direccion = models.CharField(max_length=255)
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
    empleado = models.ForeignKey(Employee, unique=True, null=True, on_delete=models.CASCADE)
    
class Rating(models.Model):
    rating = models.CharField(max_length=400)
    empleado = models.ForeignKey(Employee,unique=True,null=True,  on_delete=models.CASCADE)

    
# Contabilidad

class Ingreso(models.Model):
    Importe = models.IntegerField()
    Fecha = models.DateTimeField()
    Emisor = models.CharField(max_length=30)

class Gasto(models.Model):
    Importe = models.IntegerField()
    Fecha = models.DateTimeField()
    Destinatario = models.CharField(max_length=30)

class Produce(models.Model):
    empleado = models.ForeignKey(Employee, unique=True, on_delete=models.CASCADE)
    gasto = models.ForeignKey(Gasto, unique=True, on_delete=models.CASCADE)

class Emite(models.Model):
    empleado = models.ForeignKey(Employee, unique=True, on_delete=models.CASCADE)
    ingreso = models.ForeignKey(Ingreso, unique=True, on_delete=models.CASCADE)
    
# Logistica
#class Producto(models.Model):
 #   Nombre_Producto = models.CharField(max_length=100,null=True)
  #  Cantidad = models.IntegerField(null=True)

   # def __str__(self):
    #    return self.Nombre_Producto

class Pedido(models.Model):
    Estado = models.CharField(max_length=40)
    Precio = models.DecimalField(max_digits=10, decimal_places=2)
    Nombre_Producto = models.CharField(max_length=255, null=True)
    Cantidad = models.CharField(max_length=255, null=True)
    #Productos = models.ManyToManyField(Producto)

class Encarga(models.Model):
    usuario = models.ForeignKey(Usuario, unique=True, on_delete=models.CASCADE)
    pedido = models.ForeignKey(Pedido, unique=True, on_delete=models.CASCADE)

class Comunica(models.Model):
    restaurante = models.ForeignKey(Restaurante, unique=True, on_delete=models.CASCADE)
    pedido = models.ForeignKey(Pedido, unique=True, on_delete=models.CASCADE)

class Asigna(models.Model):
    pedido = models.ForeignKey(Pedido, unique=True, on_delete=models.CASCADE)
    empleado = models.ForeignKey(Employee, unique=True, on_delete=models.CASCADE)






