# Conexion a la base de datos
# Autor: Torres Ramos, Juan Luis
# Grupo 8 DeliveryGranada

# Paquetes usados: 
# pyodbc: pip install  pyodbc

import pyodbc

# Configuración de la conexión
host = 'oracle0.ugr.es'
port = 1521
database = 'practbd.oracle0.ugr.es'
user = 'x0596044'
password = 'x0596044x'

# Cadena de conexión
cadena_conexion = f'SERVER={host},{port};DATABASE={database};UID={user};PWD={password}'
# Intentar realizar la conexión
try:
    # Conectar a la base de datos
    connection = pyodbc.connect(cadena_conexion)
    print("Conexión exitosa.")

    # Crear un cursor para ejecutar consultas SQL
    cursor = connection.cursor()
    
    
    # SENTENCIAS SQL QUE QUERAMOS AÑADIR



except pyodbc.Error as e:
    print(f"Error de base de datos: {e}")
finally:
    # Cerrar el cursor y la conexión al finalizar
    if 'cursor' in locals():
        cursor.close()
    if 'connection' in locals():
        connection.close()
        print("Conexión cerrada.")



