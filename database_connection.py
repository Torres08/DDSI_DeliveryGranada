
#!usr/bin/python

import pymysql
import pyodbc

class BaseDatos:

    Cpedido = 0

    def __init__(self):  # Conecta con la base de datos
        # Variable que comprueba si están creadas las tablas o no
        self.tablas_creadas = False
        self.tablas_borradas = False  # True
        
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
        )

        try:
            # CONECTO CON LA BASE DE DATOS UGR
            self.cnxn = pyodbc.connect(cadena_conexion)
            # self.cnxn = pymysql.connect(host="127.0.0.1", user="root", password="1234567890", database="DDSI")
            print("CONEXION BD OK")

            # Preparo el cursor para poder acceder a las tablas
            self.cursor = self.cnxn.cursor()

        except pymysql.Error as e:
            print("OCURRIO UN ERROR AL CONECTAR: ", e)

    def verificar_conexion(self):
        if hasattr(self, 'cnxn') and self.cnxn.is_connected():
            print("La conexión está activa.")
        else:
            print("La conexión no está activa.")

def main():
    # Crear una instancia de la clase BaseDatos
    bd = BaseDatos()

    # Verificar la conexión
    bd.verificar_conexion()

    # Cerrar la conexión
    if hasattr(bd, 'cnxn') and bd.cnxn.is_connected():
        bd.cnxn.close()
        print("Conexión cerrada.")

if __name__ == "__main__":
    main()



