import csv
import datetime

import psycopg2

from examen_conmodulos.modulos.conectar_bbdd_modulo import connect_to_database
from examen_conmodulos.modulos.crea_actulizar_res_partner import crear_actualizar_res_partner
from examen_conmodulos.modulos.genera_login_modulo import generate_login
from examen_conmodulos.modulos.genera_partner_id_modulo import genera_partner_id
from examen_conmodulos.modulos.genera_password_modulo import generar_password
from examen_conmodulos.modulos.genera_signature_modulo import generar_signature

# Ruta y nombre del archivo CSV
CSV_FILE = 'modulos/usuarios.csv'


# Función para añadir o actualizar usuarios en la tabla res_users
def anadir_actulizar_usuario():
    conn = connect_to_database()
    if conn:
        try:
            cursor = conn.cursor()
            # Lectura del archivo CSV
            with open(CSV_FILE, 'r') as file:
                reader = csv.DictReader(file)
                reg_anadido = 0
                reg_modificado = 0
                for row in reader:
                    name = row['nombre']
                    last_name1 = row['apellido_1']
                    last_name2 = row['apellido_2']
                    email = row['email']
                    sexo = row['sexo']

                    # Genera el campo de inicio de sesión (login)
                    login = generate_login(name, last_name1)
                    # Genera el campo (password)
                    password = generar_password(name, last_name1, last_name2)
                    # Genera el campo (signature)
                    signature = generar_signature(last_name1, sexo)
                    # Genera el campo (parent_id)
                    partner_id = genera_partner_id(name, last_name1, last_name2, email)

                    if partner_id:
                        # crear o actulizar res_partner registro
                        partner_created = crear_actualizar_res_partner(cursor, partner_id, name, last_name1, last_name2,
                                                                       email)
                        if partner_created:
                            # Comprobar si el usario ya existe en  res_users
                            cursor.execute("SELECT id FROM res_users WHERE login = %s", (login,))
                            user_id = cursor.fetchone()

                            if user_id:
                                # El usuario ya existe, realiza una actualización
                                cursor.execute("""
                                    UPDATE res_users
                                    SET  company_id = %s, write_date = %s, password = %s, create_uid = %s,
                                    write_uid = %s, signature = %s, notification_type = %s
                                    WHERE id = %s
                                """, (1, datetime.datetime.now(), password, 2, 2, signature, 'email', user_id[0]))
                                reg_modificado += 1
                            else:
                                # El usuario no existe, crea un nuevo registro
                                cursor.execute("""
                                    INSERT INTO res_users (login, company_id, create_date, write_date, password, 
                                    create_uid, write_uid, signature, notification_type, partner_id)
                                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                                """, (login, 1, datetime.datetime.now(), datetime.datetime.now(), password,
                                      2, 2, signature, 'email', partner_id))
                                reg_anadido += 1
                        else:
                            print(f"Error: El partner con ID {partner_id} no existe en la tabla res_partner.")
                    else:
                        print("Error al generar el campo partner_id.")

            conn.commit()
            cursor.close()
            conn.close()
            # Informar de los registros añadidos y modificados
            print("Registros añadidos:", reg_anadido)
            print("Registros modificados:", reg_modificado)

        except psycopg2.Error as e:
            print("Error al ejecutar consultas SQL:", e)
    else:
        print("Error al conectar a la base de datos de Odoo.")
