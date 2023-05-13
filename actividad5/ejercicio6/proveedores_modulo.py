import csv
import psycopg2
import csv
import random
import string
import datetime


#conectamos a la base de datos de postgresql
database = input("introduzca la base datos ")
con = psycopg2.connect(database=database, user="postgres", password="2310", host="wanapito", port="5432")
print("conectado a la base de datos de ", database)

# leemos el archivo CSV
with open('clientes.csv', newline='') as archivo_csv:
    lector_csv = csv.reader(archivo_csv, delimiter=',')
    for fila in lector_csv:
        print(fila)

# Abrir el archivo CSV de clientes
with open('clientes.csv', 'r') as archivo_csv:
    lector_csv = csv.DictReader(archivo_csv)
    clientes = list(lector_csv) # Convertir el lector_csv en una lista de diccionarios

# Función para generar un nombre de usuario a partir del nombre y apellido de un cliente
def generar_nombre_usuario(nombre, apellido1):
    return (nombre[0] + apellido1).lower()

# Función para generar una contraseña aleatoria para un cliente
def generar_contrasena(nombre, apellido1, apellido2):
    # Mezclar los elementos de nombre y apellidos
    elementos = random.sample([nombre, apellido1, apellido2], 3)
    # Obtener la hora actual
    hora_actual = datetime.datetime.now().strftime('%H%M')
    # Crear la contraseña según las reglas especificadas
    contrasena = (
        elementos[0][0] + hora_actual[1:3] + elementos[1][1:3].lower() +
        hora_actual[3:] + elementos[2][3] + random.choice(['$', '%', '&'])
    )
    return contrasena

# Pedir al usuario que ingrese el nombre del cliente a modificar
nombre_cliente = input('Ingrese el nombre del cliente a modificar: ')

# Buscar el cliente en la lista de clientes
cliente_encontrado = False
for cliente in clientes:
    if cliente['Nombre'] == nombre_cliente:
        cliente_encontrado = True
        # Actualizar los datos del cliente según el archivo CSV
        cliente['Apellido1'] = input('Ingrese el primer apellido: ')
        cliente['Apellido2'] = input('Ingrese el segundo apellido: ')
        cliente['email'] = input('Ingrese el email: ')
        # Generar el nombre de usuario y la contraseña
        cliente['Nombre_usuario'] = generar_nombre_usuario(cliente['Nombre'], cliente['Apellido1'])
        cliente['Contrasena'] = generar_contrasena(cliente['Nombre'], cliente['Apellido1'], cliente['Apellido2'])
        # Mostrar los datos del cliente actualizados
        print(f'Cliente {cliente["Nombre"]} actualizado:')
        print(cliente)

# Si no se encontró el cliente, mostrar un mensaje de error
if not cliente_encontrado:
    print(f'El cliente {nombre_cliente} no fue encontrado en el archivo.')

con.commit()
con.close()