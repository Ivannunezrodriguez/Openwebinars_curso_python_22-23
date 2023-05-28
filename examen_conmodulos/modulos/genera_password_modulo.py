# Función para generar el campo  (password)
import random
import string
from datetime import datetime


def generar_password(name, last_name1, last_name2):
    # Ordenar aleatoriamente los elementos
    elementos = [name, last_name1, last_name2]
    random.shuffle(elementos)

    # Obtener la primera letra del primer elemento
    primera_letra = elementos[0][0]

    # Obtener los segundos de la hora actual
    segundos = datetime.now().second

    # Obtener las letras 2 y 3 del segundo elemento (la tercera en mayúscula)
    segundo_elemento = elementos[1]
    letras_2_3 = segundo_elemento[1:3].lower().capitalize()

    # Obtener los minutos de la hora actual
    minutos = datetime.now().minute

    # Obtener la cuarta letra del tercer elemento
    tercer_elemento = elementos[2]
    cuarta_letra = tercer_elemento[3]

    # Escoger al azar uno de los símbolos: "$", "%", "&"
    simbolos = ["$", "%", "&"]
    simbolo_azar = random.choice(simbolos)

    # Generar la contraseña
    password = f"{primera_letra}{segundos}{letras_2_3}{minutos}{cuarta_letra}{simbolo_azar}"

    # Verificar si la contraseña cumple con los requisitos mínimos
    if len(password) < 8 or not any(c.islower() for c in password) or not any(
            c.isupper() for c in password) or not any(c.isdigit() for c in password) or not any(c in string.punctuation
                                                                                                for c in password):
        password = "Cam5iar$"

    return password
