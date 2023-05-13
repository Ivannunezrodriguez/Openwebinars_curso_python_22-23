#Pide al usuario dos pares de números x1,y2 y x2,y2, que representen dos puntos en el plano. Calcula y muestra la distancia entre ellos.
import math
x1=float(input("introduce x1"))
x2=float(input("introduce x2"))
y2=float(input("introduce y2"))
y1=float(input("introduce y1"))
math.dist(x1,y2)

#Realizar un algoritmos que lea un número y que muestre su raíz cuadrada y su raíz cúbica. Python3 no tiene ninguna función predefinida que permita calcular la raíz cúbica, ¿Cómo se puede calcular?
import math
numero1=float(input("introduce el numero"))
resultado=print("el resulatdo de la raiz cuadrada es ",math.sqrt(numero1),"y de la raiz cubica es ",(numero1**(1. / 3.)))

#Dado un número de dos cifras, diseñe un algoritmo que permita obtener el número invertido. Ejemplo, si se introduce 23 que muestre 32.
numero=input("introduce un numero de 2 cifras")
resultado=print(numero[1],numero[0])


#Dadas dos variables numéricas A y B, que el usuario debe teclear, se pide realizar un algoritmo que intercambie los valores de ambas variables y muestre cuanto valen al final las dos variables.
numeroA =int(input("introduca el numero a "))
numeroB =int(input("introduca el numero b "))
aux=numeroA
numeroA=numeroB
numeroB=aux
resultado =print("el numero a",numeroA  ,"el numero b ",aux)
