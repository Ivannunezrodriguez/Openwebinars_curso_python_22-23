import datetime


def crear_actualizar_res_partner(cursor, partner_id, name, last_name1, last_name2, email):
    # Check if the res_partner record already exists
    cursor.execute("SELECT id FROM res_partner WHERE id = %s", (partner_id,))
    partner_exists = cursor.fetchone()

    if partner_exists:
        # Update the existing res_partner record
        cursor.execute("""
            UPDATE res_partner
            SET name = %s, display_name = %s, write_date = %s, lang = %s, email = %s,
            commercial_partner_id = %s, create_uid = %s, write_uid = %s
            WHERE id = %s
        """, (f"{name} {last_name1} {last_name2}", f"{name} {last_name1} {last_name2}",
              datetime.datetime.now(), 'es_ES', email, 2, 2, 2, partner_id))
    else:
        # Create a new res_partner record
        cursor.execute("""
            INSERT INTO res_partner (id, name, display_name, create_date, write_date, lang, email,
            commercial_partner_id, create_uid, write_uid)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """, (partner_id, f"{name} {last_name1} {last_name2}", f"{name} {last_name1} {last_name2}",
              datetime.datetime.now(), datetime.datetime.now(), 'es_ES', email, 2, 2, 2))

    return True  # Indicates successful creation or update
