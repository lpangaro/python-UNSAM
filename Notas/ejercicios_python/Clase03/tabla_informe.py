#informe.py

#Author: Lucas Pangaro
#Mail: Pangaro.lucas@gmail.com
#Date: 25/3/21


# ..:EJERCICIO 3.13:..
#%%
import csv
def leer_precios(archivo):
    '''Creo un diccionario con los productos y precios de venta del negocio'''
    d = {}
    with open (archivo, "rt") as f:
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
        renglones = csv.reader(f)
        headers = next(renglones)

        for row in renglones:  
            s = {
            'nombre' : row[0],
            'cajones' : int(row[1]),
            'precio' : float(row[2])  
            }

            lista_camion.append(s)

    return lista_camion

#%%
def hacer_informe(camion, dic_precios):
    lista_de_tuplas = []
    cambio = 0.0
    for s in camion:
        cambio = dic_precios[s['nombre']] - s['precio']
        tupla = (s['nombre'], s['cajones'], s['precio'], cambio)
        lista_de_tuplas.append(tupla)
  
    return lista_de_tuplas

#%%
camion = leer_camion('../Data/camion.csv')
dic_precios = leer_precios('../Data/precios.csv')
costo_camion = 0.0
ventas = 0.0
ganancia = 0.0

headers = ('Nombre', 'Cajones', 'Precio', 'Cambio')
informe = hacer_informe(camion, dic_precios)

print (f'\x1b[1;35m {headers[0]:>10s} {headers[1]:>10s} {headers[2]:>10s} {headers[3]:>10s}') #\x1b[1;35m  codigo de color
print(f' {"":->44} \x1b[0m') #linea horizontal


for nombre, cajones, precio, cambio in informe:
    str_precio = '$'+ str(precio)
    print(f'{nombre:>10s} {cajones:>10d}  {str_precio:>10s} {cambio:>10.2f}')
