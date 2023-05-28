# Función para generar el campo  (signature)
def generar_signature(last_name1, sexo):
    if sexo == "H":
        signature = "Sr. " + last_name1
    elif sexo == "M":
        signature = "Sra. " + last_name1
    else:
        signature = ""
    return signature
