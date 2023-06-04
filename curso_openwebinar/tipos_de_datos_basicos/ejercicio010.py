# Escribir un programa que pregunte al usuario su nombre, y luego lo salude.
nombre = input("introduce tu nombre")
print("hola", nombre)
# Calcular el perímetro y área de un rectángulo dada su base y su altura.
base = int(input("introduce la base "))
altura = int(input("introduce su altura"))
resultado = base * altura
print("el resultado es ", resultado)
# Realiza un programa que reciba una cantidad de minutos y muestre por pantalla a cuantas horas y minutos corresponde.
# Por ejemplo: 1000 minutos son 16 horas y 40 minutos.
minuto = int(input("introduzca minutos"))
print("son ", (minuto // 60), "horas")
# Un vendedor recibe un sueldo base más un 10% extra por comisión de sus ventas,
# el vendedor desea saber cuanto dinero obtendrá por concepto de comisiones por las 
# tres ventas que realiza en el mes y el total que recibirá en el mes tomando en cuenta su sueldo base y comisiones.
sueldo_base = 1000
comisión = int(input("introduzca el número de ventas "))

extra = sueldo_base * 0.10
print("el sueldo base con ", comisión, "ventas es", sueldo_base + (extra * comisión))
