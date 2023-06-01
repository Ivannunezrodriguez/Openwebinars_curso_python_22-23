# dado los catetos de un triangulo rectángulo
# calcula su hipotenusa
import math

cateto1 = float(input("introduce el cateto 1"))
cateto2 = float(input("introduce el cateto 2"))
hipotenusa = math.sqrt(math.pow(cateto1, 2) + math.pow(cateto2, 2))
print("el valor de la hipotenusa es %2f" % hipotenusa)
# Dados dos números, mostrar la suma, resta, división y multiplicación de ambos.
numero1 = int(input("introduce el numero 1"))
numero2 = int(input("introduce el numero 2"))
suma = numero1 + numero2
multiplicación = numero1 * numero2
resta = numero1 - numero2
división = numero1 / numero2
print("el resultado son ", "suma", suma, " resta", resta, " division", división, " multiplicación", multiplicación)
# Escribir un programa que convierta un valor dado en grados Fahrenheit a grados Celsius. Recordar que la fórmula
# para la conversión es:
grado = float(input("introduzca los grados fahrenheit"))
print("la conversion es %f" % ((grado - 32) * 5 / 9), "grados celsius")
# Calcular la media de tres números pedidos por teclado.
numero1 = int(input("introduzca numero1"))
numero2 = int(input("introduzca numero2"))
numero3 = int(input("introduzca numero3"))
print("la media es ", ((numero1 + numero2 + numero3) / 3))
