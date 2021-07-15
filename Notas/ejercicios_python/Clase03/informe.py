#informe.py

#Author: Lucas Pangaro
#Mail: Pangaro.lucas@gmail.com
#Date: 25/3/21

# ..:EJERCICIO 3.9:..
'''Modificá el programa informe.py que escribiste antes (ver Ejercicio 2.18) 
para que use esta técnica para elegir las columnas a partir de sus encabezados.

Probá correr el programa informe.py sobre el archivo Data/fecha_camion.csv
 y fijate si da la misma salida que antes.'''
#%%
import csv
def leer_precios(archivo):
    '''Creo un diccionario con los productos y precios de venta del negocio'''
    d = {}
    with open (archivo, 'rt') as f:
        renglones = csv.reader(f)
        for row in renglones:
            try:
                d[row[0]] = float(row[1])
            except :
                pass
    return d

#%%
def leer_camion(archivo):
    '''Creo una lista de diccionarios, cada elemento de la lista contiene un diccionaria con nombre, cajones y precio'''
    lista_camion = []
    with open (archivo, 'rt') as f:
        filas = csv.reader(f)
        headers = next(filas)

        for n_filas, fila in enumerate(filas, start=1):
            record = dict(zip(headers, fila))  
            try:
                lista_camion.append(record)
                
            except ValueError:
                print(f'Fila {n_filas}: No puede interpretar: {fila}')

    return lista_camion

#%%
camion = leer_camion('../Data/fecha_camion.csv')
dic_precios = leer_precios('../Data/precios.csv')
costo_camion = 0.0
ventas = 0.0
ganancia = 0.0

for lista in camion:
    if lista['nombre'] in dic_precios: #en cada iteracion pregunto si el nombre del producto de la lista coincide con algun key del diccionario 
        costo_camion += float(lista['precio']) * int(lista['cajones']) 
        ventas += dic_precios[lista['nombre']]  * int(lista['cajones']) 

ganancia = ventas - costo_camion

if ganancia > 0:
    print(f'El vendedor recaudó ${ventas} y pagó un total de ${costo_camion} por la mercaderia. \nPor lo tanto obtuvo una GANANCIA de ${ganancia:.2f}')

else: #perida
    print(f'El vendedor recaudó ${ventas} y pagó un total de ${costo_camion} por la mercaderia. \nPor lo tanto tuvo una PERDIDA de ${ganancia:.2f}')

