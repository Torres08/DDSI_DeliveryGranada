# version cx_Oracle

# pip install cx_Oracle
# python database_connection.py

import cx_Oracle

# Configuración de la conexión
dsn = cx_Oracle.makedsn('oracle0.ugr.es', 1521, service_name='practbd.oracle0.ugr.es')
usuario = 'x0596044'
contraseña = 'x0596044'

# Cadena de conexión
cadena_conexion = f'{usuario}/{contraseña}@{dsn}'


# Configuración de la conexión
host = 'oracle0.ugr.es'
port = 1521
service_name = 'practbd.oracle0.ugr.es'
usuario = 'x0596044'
contraseña = 'x0596044'

# Cadena de conexión
cadena_conexion2 = f'{usuario}/{contraseña}@{host}:{port}/{service_name}'

try:
    # Conectar a la base de datos
    connection = cx_Oracle.connect(cadena_conexion2)
    print("Conexión exitosa.")

    # Crear un cursor para ejecutar consultas SQL
    cursor = connection.cursor()
    
    # Aquí puedes agregar tus sentencias SQL
    
except cx_Oracle.Error as e:
    print(f"Error de base de datos: {e}")
finally:
    # Cerrar el cursor y la conexión al finalizar
    if 'cursor' in locals():
        cursor.close()
    if 'connection' in locals():
        connection.close()
        print("Conexión cerrada.")