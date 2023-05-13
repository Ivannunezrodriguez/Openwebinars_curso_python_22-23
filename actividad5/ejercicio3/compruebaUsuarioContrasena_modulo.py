#importamos
import psycopg2
import re
from actividad5.ejercicio1 import compruebaNombre_modulo
from actividad5.ejercicio2 import compruebaContrasena_modulo
#creamos el codigo necesario
def validar_credenciales():
   
    if compruebaNombre_modulo.resultado==0 and compruebaContrasena_modulo.resultado:
        print("Credenciales válidas")
    else :
        print("Credenciales no válidas")
 
#conectamos a la base de datos de postgresql
database = input("introduzca la base datos ")
con = psycopg2.connect(database=database, user="postgres", password="2310", host="wanapito", port="5432")
print("conectado a la base de datos de ", database)

#ejecutamos el cursor
cur = con.cursor()
cur.execute("INSERT INTO res_users (login,password,company_id,partner_id) VALUES (%s,%s,'%s','%s')",
            (compruebaNombre_modulo.usuario,compruebaContrasena_modulo.password,1,9))
con.commit()
print("Guardado correctamente ")
con.close()



