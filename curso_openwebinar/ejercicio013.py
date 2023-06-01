# Dos vehículos viajan a diferentes velocidades (v1 y v2) y están distanciados por una distancia d. El que está
# detrás viaja a una velocidad mayor. Se pide hacer un algoritmo para ingresar la distancia entre los
# dos vehículos (# km) y sus respectivas velocidades (km/h) y con esto determinar y
# mostrar en que tiempo (minutos) alcanzará el
# vehículo más rápido al otro.
v1 = float(input("introduzca la velocidad"))
v2 = float(input("introduzca la velocidad"))
distancia = float(input("introduzca la distancia"))
cuenta_v1 = float((distancia / v1) * 60)
cuenta_v2 = float((distancia / v2) * 60)
print("si la velocidad de v1", v1, "y la distancia ", distancia, "es",
      cuenta_v1, "si la velocidad de v2", v2, "y la distancia ", distancia, "es", cuenta_v2, "por lo que tardaran ",
      (cuenta_v1 - cuenta_v2))

# Un ciclista parte de una ciudad A las HH horas, MM minutos y SS segundos. El tiempo de viaje hasta llegar a otra
# ciudad B es de T segundos. Escribir un algoritmo que determine la hora de llegada a la ciudad B.
hora = float(input("introduzca las horas"))
minuto = float(input("introduzca los minutos"))
segundo = float(input("introduzca los segundos"))
tiempo = float(input("tiempo que has tardado en segundos "))
resultado = int(((((hora * 60) + minuto) * 60) + segundo) + tiempo)
print(resultado // 3600), ((resultado % 3600) // 60), ((resultado & 3600) % 60)

# Pedir el nombre y los dos apellidos de una persona y mostrar las iniciales.
nombre = input("introduzca sun nombre")
apellido1 = input("introduzca sus apellidos")
apellido2 = input("introduzca sus apellidos")
inicial = nombre[0]
inicial = inicial + apellido1[0]
inicial = inicial + apellido2[0]
print("las iniciales son", inicial.upper())

# Escribir un algoritmo para calcular la nota final de un estudiante, considerando que: por cada respuesta correcta 5
# puntos, por una incorrecta -1 y por respuestas en blanco 0. Imprime el resultado obtenido por el estudiante.
respuesta_correcta = int(input("indique el numero de respuestas "))
respuesta_incorrecta = int(input("indique el numero de respuestas "))
respuesta_blanco = int(input("indique el numero de respuestas "))
correcta = respuesta_correcta * 5
incorrecta = respuesta_incorrecta * -1
blanco = respuesta_blanco * 0
print(correcta + incorrecta + blanco)

# Diseñar un algoritmo que nos diga el dinero que tenemos (en euros y céntimos) después de pedirnos cuantas monedas
# tenemos (de 2 €, 1 €, 50 céntimos, 20 céntimos o 10 céntimos).
cantidad2 = float(input("introduzca cuantas monedas tiene de 2 "))
cantidad1 = float(input("introduzca cuantas monedas tiene de 1"))
cantidad50 = float(input("introduzca cuantas monedas tiene de 50"))
cantidad20 = float(input("introduzca cuantas monedas tiene de 20"))
cantidad10 = float(input("introduzca cuantas monedas tiene de 10"))
moneda2 = 2 * cantidad2
moneda1 = 1 * cantidad1
moneda10 = 0.10 * cantidad10
moneda50 = 0.50 * cantidad50
moneda20 = 0.20 * cantidad20
print(moneda1 + moneda2 + moneda10 + moneda20 + moneda50, "son los euros que tiene ")
