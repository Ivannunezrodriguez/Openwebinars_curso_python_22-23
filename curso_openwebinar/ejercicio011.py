# Una tienda ofrece un descuento del 15% sobre el total de la compra y un cliente desea saber cuanto deberá pagar
# finalmente por su compra.
precio = float(input("introduzca el valor del producto "))
descuento = precio * 0.15
print("el precio final es ", (precio - descuento), "sobre el precio original que es ", precio)
# Un alumno desea saber cuál será su calificación final en la materia de Algoritmos. Dicha calificación se compone de
# los siguientes porcentajes: 55% del promedio de sus tres calificaciones parciales. 30% de la calificación del
# examen_con1_modulos.py final. 15% de la calificación de un trabajo final.
import math

trabajo_final = float(input("introduzca nota trabajo final "))
examen_final = float(input("introduzca nota examen_con_modulos.py final "))
parcial1 = float(input("introduzca nota parcial1"))
parcial2 = float(input("introduzca nota parcial2"))
parcial3 = float(input("introduzca nota parcial3"))
print("el resultado es %.2f " % (
    ((trabajo_final * 0.15) + (examen_final * 0.30) + (((parcial1 + parcial2 + parcial3) / 3) * 0.55))))
# Pide al usuario dos números y muestra la “distancia” entre ellos (el valor absoluto de su diferencia, de modo que
# el resultado sea siempre positivo).
print("introduzca el numero1")
numero1 = float(input())
print("introduzca el numero2")
numero2 = float(input())
resultado = math.dist(numero1, numero2)
