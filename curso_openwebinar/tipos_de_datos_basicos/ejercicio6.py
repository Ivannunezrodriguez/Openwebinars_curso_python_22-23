nombre = input("introduzca nombre")
print(nombre)
# con input introducimos datos
# tenemos que indicar que tipo de dato queremos recoger
edad = int(input("introduzca edad"))
print(edad)
print(type(edad))
# se puede unir con comas int con string
print("hola son ", 6, "de la tarde")
# se pude unir sumando indicando el tipo de dato
print("hola son las " + str(6) + " de la tarde ")
# %s se muestra como string
# %d se muestra dato 
# %f se muestra con numero real
print("%d %f %s " % (2.5, 2.5, 2.5))
# trasladamos el dato de parenthesis después del porcentaje
print("el producto %s cantidad= %d precio=%.2f " % ("cesta", 23, 13.456))
