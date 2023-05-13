#importamos
import csv
import psycopg2

#conectamos a la base de datos de postgresql
database = input("introduzca la base datos ")
con = psycopg2.connect(database=database, user="postgres", password="2310", host="wanapito", port="5432")
print("conectado a la base de datos de ", database)

#ejecutamos el cursor
cur = con.cursor()
cur.execute("SELECT stock_quant.product_id,product_template.default_code, product_template.name, stock_quant.quantity "
            " FROM product_template "
            " JOIN product_product "
            " ON product_template.id = product_product.product_tmpl_id "
            " JOIN stock_quant "
            " ON product_product.id = stock_quant.product_id   "
            " where stock_quant.quantity>=0 "
            " ORDER BY stock_quant.product_id")

 # Obtenemos los resultados y los escribimos en el archivo CSV
resultados = cur.fetchall()

# Abrimos el archivo CSV en modo escritura
with open('stock.csv', mode='w', newline='') as file:

    # Creamos el objeto writer de la librería csv
    writer = csv.writer(file, delimiter=',')

    # Escribimos la cabecera del archivo CSV
    for row in resultados:
        writer.writerow(["ID =",row[0],"Definicion =", row[1],"Nombre =" , row[2] ,"Cantidad =" , row[3]])
# Cerramos la conexión a la base de datos
file.close()
con.close()

# Abre el archivo CSV
with open('stock.csv', 'r') as file:
    # Lee el archivo CSV
    csv_reader = csv.reader(file)

    # Define el criterio de búsqueda
    criterio = input('valor buscado')

    # Recorre cada línea del archivo CSV
    for linea in csv_reader:
        # Verifica si la línea coincide con el criterio de búsqueda
        if criterio in linea:
            # Almacena la línea que coincide en una variable
            linea_encontrada = linea
            # Sale del bucle
            break

    # Verifica si se encontró la línea buscada
    if 'linea_encontrada' in locals():
        # Si se encontró la línea, muestra la línea
        print(linea_encontrada)
    else:
        # Si no se encontró la línea, muestra un mensaje de error
        print('No se encontró ninguna línea que coincida con el criterio de búsqueda.')





