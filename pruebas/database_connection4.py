# Conexion a la base de datos
# Autor: Torres Ramos, Juan Luis
# Grupo 8 DeliveryGranada

# Paquetes usados: 
# pyodbc: pip install  pyodbc

import pyodbc

# Configuración de la conexión
driver = 'ODBC Driver 18 for SQL Server'  # Asegúrate de usar el nombre correcto del driver
host = 'oracle0.ugr.es'
port = 1521
database = 'practbd.oracle0.ugr.es'
user = 'x0596044'
password = 'x0596044'

# Cadena de conexión
cadena_conexion = (
    f'DRIVER={driver};'
    f'SERVER={host},{port};'
    f'DATABASE={database};'
    f'UID={user};'
    f'PWD={password};'
    'Timeout=600;'  # Ajusta el valor de Timeout según tus necesidades
)

# conectar a una base de datos local


try:
    # Conectar a la base de datos
    connection = pyodbc.connect(cadena_conexion)
    print("Conexión exitosa.")

    # Crear un cursor para ejecutar consultas SQL
    cursor = connection.cursor()
    
    # Aquí puedes agregar tus sentencias SQL
    
except pyodbc.Error as e:
    print(f"Error de base de datos: {e}")
finally:
    # Cerrar el cursor y la conexión al finalizar
    if 'cursor' in locals():
        cursor.close()
    if 'connection' in locals():
        connection.close()
        print("Conexión cerrada.")


