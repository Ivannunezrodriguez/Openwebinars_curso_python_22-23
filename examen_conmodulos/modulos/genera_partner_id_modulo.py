# Función para generar el campo (partner_id)
import datetime

import psycopg2

from examen_conmodulos.modulos.conectar_bbdd_modulo import connect_to_database


def genera_partner_id(name, last_name1, last_name2, email):
    conn = connect_to_database()
    if conn:
        try:
            cursor = conn.cursor()

            # Verificar si el partner ya existe en la tabla res_partner
            cursor.execute("SELECT id FROM res_partner WHERE name = %s", (f"{name} {last_name1} {last_name2}",))
            partner_id = cursor.fetchone()

            if partner_id:
                return partner_id[0]  # Devolver el ID existente

            # El partner no existe, crear un nuevo registro
            cursor.execute("""
                INSERT INTO res_partner (name, display_name, create_date, write_date, lang, email,
                commercial_partner_id, create_uid, write_uid)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
                RETURNING id
            """, (f"{name} {last_name1} {last_name2}", f"{name} {last_name1} {last_name2}", datetime.datetime.now(),
                  datetime.datetime.now(), 'es_ES', email, 2, 2, 2))

            partner_id = cursor.fetchone()
            if partner_id:
                return partner_id[0]  # Devolver el nuevo ID del partner creado

            conn.commit()
            cursor.close()
            conn.close()

        except psycopg2.Error as e:
            print("Error al ejecutar consultas SQL:", e)
    else:
        print("Error al conectar a la base de datos de Odoo.")

    return None  # Devolver None si no se pudo obtener o crear el partner
