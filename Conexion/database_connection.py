import pyodbc

# Configuración de la conexión
driver = 'ODBC Driver 18 for SQL Server'  # Asegúrate de usar el nombre correcto del driver
host = 'oracle0.ugr.es'
port = 1521
database = 'practbd.oracle0.ugr.es'

user = 'x0596044'
password = 'x0596044x'

# Cadena de conexión
cadena_conexion = f'SERVER={host},{port};DATABASE={database};UID={user};PWD={password}'
# Intentar realizar la conexión
cadena_conexion = (
    f'DRIVER={driver};'
    f'SERVER={host},{port};'
    f'DATABASE={database};'
    f'UID={user};'
    f'PWD={password};'
    'Timeout=600;'  # Ajusta el valor de Timeout según tus necesidades
)

try:
    # Conectar a la base de datos
    connection = pyodbc.connect(cadena_conexion)

try:
    # Crear un cursor para ejecutar consultas SQL
    cursor = connection.cursor()
    
    # Aquí puedes agregar tus sentencias SQL
    
    # SENTENCIAS SQL QUE QUERAMOS AÑADIR



except pyodbc.Error as e:
    print(f"Error de base de datos: {e}")
finally:

@@ -41,4 +46,3 @@ finally:
        print("Conexión cerrada.")