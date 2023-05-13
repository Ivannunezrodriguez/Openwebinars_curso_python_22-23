#importamos
import psycopg2
import re
#creamos el codigo necesario
usuario = input("introduzca el nombre de usuario")
def validar_nombre_usuario(usuario):
    if len(usuario) < 6:
        return 1
    elif len(usuario) > 12:
        return 2
    elif not re.match("^[a-zA-Z0-9_]*$", usuario):
        return 3
    else:
        return 0

resultado = validar_nombre_usuario(usuario)

if resultado == 0:
    print("El nombre de usuario es válido.")
elif resultado == 1:
    print("El nombre de usuario debe contener al menos 6 caracteres.")
elif resultado == 2:
    print("El nombre de usuario no puede contener más de 12 caracteres.")
elif resultado == 3:
    print("El nombre de usuario puede contener solo letras y números.")

#conectamos a la base de datos de postgresql
database = input("introduzca la base datos ")
con = psycopg2.connect(database=database, user="postgres", password="2310", host="wanapito", port="5432")
print("conectado a la base de datos de ", database)

#ejecutamos el cursor
cur = con.cursor()
cur.execute("INSERT INTO res_users (login,company_id,partner_id) VALUES (%s,'%s','%s')",(usuario,1,9))
con.commit()
print("Guardado correctamente ")
con.close()