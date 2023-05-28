# Función para conectar a la base de datos de Odoo
import psycopg2

# Datos de conexión a la base de datos de Odoo
DB_NAME = input("Introduzca base de datos ")
DB_USER = input("Introduzca usuario ")
DB_PASSWORD = input("Introduzca password ")
DB_HOST = input("Introduzca conexion ")
DB_PORT = input("introduzca puerto por def '5432' ")


def connect_to_database():
    try:
        conn = psycopg2.connect(database=DB_NAME, user=DB_USER, password=DB_PASSWORD, host=DB_HOST, port=DB_PORT)
        return conn
    except psycopg2.Error as e:
        print("Error al conectar a la base de datos de Odoo:", e)
