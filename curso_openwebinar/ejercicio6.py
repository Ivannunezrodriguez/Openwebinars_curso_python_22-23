nombre =input("intorduzca nombre")
print(nombre)
#con input introducimos datos 
#tenemso que indicar que tipo de dato queremos recoger 
edad= int (input("introduzca edad"))
print(edad)
print(type(edad))  
#se puede unir con comas int con string     
print("hola son ", 6 ,"de la tarde")
#se pude unir sumando indicando el tipo de dato
print("hola son las "+ str(6)+" de la tarde ")
# %s se muestar como string
# %d se muestra dato 
# %f se muesta con numero real 
print("%d %f %s " % (2.5,2.5,2.5))
#trasladamos el datos de parentesis despues del porcentaje 
print("el productos %s cantidad= %d precio=%.2f "%("cesta",23,13.456))