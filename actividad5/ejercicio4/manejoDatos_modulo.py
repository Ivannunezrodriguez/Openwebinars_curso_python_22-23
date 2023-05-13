#importamos
import csv
#creamos el codigo necesario
def crear_tabla():
    tabla = {}
    while True:
        nombre = input("Ingrese el nombre: ")
        if not nombre:
            break
        apellidos = input("Ingrese los apellidos: ")
        fecha_nacimiento = input("Ingrese la fecha de nacimiento: ")
        direccion = input("Ingrese la dirección: ")
        contrasena = input("Ingrese la contraseña: ")
        tabla[nombre] = {
            "apellidos": apellidos,
            "fecha_nacimiento": fecha_nacimiento,
            "direccion": direccion,
            "contrasena": contrasena
        }
    return tabla

def buscar_en_tabla(tabla, clave):
    for nombre, datos in tabla.items():
        if clave in nombre or clave in datos["apellidos"]:
            print("Nombre: ", nombre)
            print("Apellidos: ", datos["apellidos"])
            print("Fecha de nacimiento: ", datos["fecha_nacimiento"])
            print("Dirección: ", datos["direccion"])
            print("Contraseña: ", datos["contrasena"])

def agregar_a_csv(tabla, archivo_csv):
    with open(archivo_csv, "a", newline="") as csv_file:
        writer = csv.writer(csv_file)
        for nombre, datos in tabla.items():
            row = [nombre, datos["apellidos"], datos["fecha_nacimiento"], datos["direccion"], datos["contrasena"]]
            writer.writerow(row)

def recuperar_de_csv(archivo_csv):
    tabla = {}
    with open(archivo_csv, "r") as csv_file:
        reader = csv.reader(csv_file)
        for row in reader:
            nombre, apellidos, fecha_nacimiento, direccion, contrasena = row
            tabla[nombre] = {
                "apellidos": apellidos,
                "fecha_nacimiento": fecha_nacimiento,
                "direccion": direccion,
                "contrasena": contrasena
            }
    return tabla

def menu():
    tabla = {}
    while True:
        print("1. Crear tabla")
        print("2. Buscar en tabla")
        print("3. Agregar a archivo CSV")
        print("4. Recuperar desde archivo CSV")
        print("0. Salir")
        opcion = int(input("Ingrese una opción: "))
        if opcion == 1:
            tabla = crear_tabla()
        elif opcion == 2:
            clave = input("Ingrese una nombre : ")
            buscar_en_tabla(tabla, clave)
        elif opcion == 3:
            archivo_csv = input("Ingrese el nombre del archivo CSV: ")
            agregar_a_csv(tabla, archivo_csv)
        elif opcion == 4:
            archivo_csv = input("Ingrese el nombre del archivo CSV: ")
            tabla = recuperar_de_csv(archivo_csv)
        elif opcion == 0:
            break
        else:
            print("Opción no válida")

menu()

