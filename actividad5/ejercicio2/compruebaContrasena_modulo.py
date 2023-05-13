#importamos
import re
import psycopg2
from actividad5.ejercicio1 import compruebaNombre_modulo
#creamos el codigo necesario
def validar_contrasena(password):

    if len(password) < 8:
        return False
    elif not re.search("[a-z]", password):
        return False
    elif not re.search("[A-Z]", password):
        return False
    elif not re.search("[0-9]", password):
        return False
    elif re.search("\s", password):
        return False
    elif re.search("\W", password):
        return True
    else:
        return False


print("Introduzca Contraseña")
password = input()
resultado = validar_contrasena(password)

if resultado==True:
    print("Contraseña válida.")
else:
    print("Contraseña no válida.")

#conectamos a la base de datos de postgresql
database = input("introduzca la base datos ")
con = psycopg2.connect(database=database, user="postgres", password="2310", host="wanapito", port="5432")
print("conectado a la base de datos de ", database)

#ejecutamos el cursor
cur = con.cursor()
cur.execute("INSERT INTO res_users (login,password,company_id,partner_id,notification_type) VALUES (%s,'%s','%s',%s)",(compruebaNombre_modulo.usuario,password,1,9,"email"))
con.commit()
print("Guardado correctamente ")
con.close()