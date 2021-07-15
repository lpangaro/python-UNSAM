#informe.py

#Author: Lucas Pangaro
#Mail: Pangaro.lucas@gmail.com
#Date: 20/3/21

#%%
# ..:EJERCICIO 2.15:..
'''El archivo Data/camion.csv contiene la lista de cajones cargados en un camión. 
En el Ejercicio 2.6 de la sección anterior escribiste una función 
costo_camion(nombre_archivo) que leía el archivo y realizaba un cálculo.'''
'''
import csv
def leer_camion(archivo):
    lista_camion = []
    with open (archivo, 'rt') as f:
        renglones = csv.reader(f)
        headers = next(renglones)

        for row in renglones:   #ya me deja la lista. no necesito de split
            lote = (row[0], int(row[1]), float(row[2]))
            lista_camion.append(lote)

    return lista_camion

total = 0.0
camion = leer_camion('../data/camion.csv')

for nombre, cajones, precio in camion:
    total += cajones*precio

print('Costo Toatal: ',total)
'''
#%%
# ..:EJERCICIO 2.16:..
'''Tomá la función que escribiste en el ejercicio anterior y modificala para 
representar cada cajón del camión con un diccionario en vez de una tupla. 
En este diccionario usá los campos "nombre", "cajones" y "precio" para
representar las diferentes columnas del archivo de entrada'''
'''
import csv
def leer_camion(archivo):
    lista_camion = []
    with open (archivo, 'rt') as f:
        renglones = csv.reader(f)
        headers = next(renglones)

        for row in renglones:   #ya me deja la lista. no necesito de split

            s = {
            'nombre' : row[0],
            'cajones' : int(row[1]),
            'precio' : float(row[2])  
            }

            lista_camion.append(s)

    return lista_camion

total = 0.0
camion = leer_camion('../data/camion.csv')

for s in camion:
    total += s['cajones']*s['precio']

from pprint import pprint
pprint(camion)
print('Costo Toatal: ',total)
'''

# ..:EJERCICIO 2.17:..
'''
Del ejercicio 2.7 Escribí una función leer_precios(nombre_archivo) que a partir 
de un conjunto de precios como éste arme un diccionario donde las claves sean 
los nombres de frutas y verduras, y los valores sean los precios por cajón.
'''
'''
import csv
def leer_precios(archivo):

    d = {}
    with open (archivo, "rt") as f:
        renglones = csv.reader(f)
        for row in renglones:
            try:
                d[row[0]] = float(row[1])
            except :
                pass
    return d

precios = leer_precios('../Data/precios.csv')

print(precios)
'''

# ..:EJERCICIO 2.18:..
'''juntá todo el trabajo que hiciste recién en tu programa informe.py 
(usando las funciones leer_camion() y leer_precios()) y completá el programa 
para que con los precios del camión (Ejercicio 2.16) y los de venta en el 
negocio (Ejercicio 2.17) calcule lo que costó el camión, lo que se recaudó 
con la venta, y la diferencia. ¿Hubo ganancia o pérdida? 
El programa debe imprimir por pantalla un balance con estos datos.'''
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
camion = leer_camion('../Data/camion.csv')
dic_precios = leer_precios('../Data/precios.csv')
costo_camion = 0.0
ventas = 0.0
ganancia = 0.0

for s in camion:
    #print(s['nombre'])  #aca tengo el nombre de los productos en cada iteracion del for
    if s['nombre'] in dic_precios: #en cada iteracion pregunto si el nombre del producto de la lista coincide con algun key del diccionario
        costo_camion += (s['precio']) * s['cajones'] 
        ventas += dic_precios[s['nombre']]  * s['cajones'] 

ganancia = ventas - costo_camion

if ganancia > 0:
    print(f'El vendedor recaudó ${ventas} y pagó un total de ${costo_camion} por la mercaderia. \nPor lo tanto obtuvo una GANANCIA de ${ganancia:.2f}')

else: #perida
    print(f'El vendedor recaudó ${ventas} y pagó un total de ${costo_camion} por la mercaderia. \nPor lo tanto tuvo una PERDIDA de ${ganancia:.2f}')


'''
Output
El vendedor recaudó $62986.1 y pagó un total de $47671.15 por la mercaderia.
Por lo tanto obtuvo una GANANCIA de $15314.95
'''