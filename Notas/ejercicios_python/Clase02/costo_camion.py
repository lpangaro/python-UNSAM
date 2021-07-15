#costo_camion.py

#Author: Lucas Pangaro
#Mail: Pangaro.lucas@gmail.com
#Date: 20/3/21

# ..:EJERCICIO 2.2:..
'''
total = 0
with open ('../data/camion.csv', "rt") as f:
    headers = next(f)
    for line in f:
        row = line.split(',')
        total += float(row[1]) * float(row[2])
    print('Costo Total:', total)
'''
# ..:EJERCICIO 2.6:..
''' Transformá el programa costo_camion.py (que escribiste en el Ejercicio 2.2 de la sección anterior) 
en una función costo_camion(nombre_archivo). Esta función recibe un nombre de archivo como entrada, 
lee la información sobre los cajones que cargó el camión y devuelve el costo 
de la carga de frutas como una variable de punto flotante'''

'''
def costo_camion(archivo):
    total = 0
    with open ('../data/camion.csv', "rt") as f:
        headers = next(f)
        for line in f:
            row = line.split(',')
            total += float(row[1]) * float(row[2])
    return (total)

costo = costo_camion('../data/camion.csv')
print('Costo TOATAL:', costo)
'''

# ..:EJERCICIO 2.9:..
'''Modificá tu programa costo_camion.py para que use el módulo csv para leer los 
archivos CSV y probalo en un par de los ejemplos anteriores.'''

import csv
def costo_camion(archivo):
    total = 0
    f = open(archivo, 'rt')
    renglones = csv.reader(f)
    headers = next(renglones)

    for row in renglones:   #ya me deja la lista. no necesito de split
        total += float(row[1]) * float(row[2])
    
    return(total)


costo = costo_camion('../Data/camion.csv')
print('Costo TOATAL:', costo)

'''
Output
Costo TOATAL: 47671.15 
'''