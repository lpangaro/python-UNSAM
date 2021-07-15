# -*- coding: utf-8 -*-
"""
Created on Sun Mar 28 14:06:07 2021

@author: panga
"""

#%%
# ..:EJERCICIO 3.18:..
import csv
def leer_parque (archivo, parque):
    
    file = open (archivo, encoding="utf8")
    
    filas = csv.reader(file)
    header = next (filas)
    
    lista = []
    
    for n_fila, fila in enumerate(filas,start=1):
        
        record = dict( zip(header, fila) ) 
        
        try:
            if record['espacio_ve'] == parque:
                lista.append(record)
             
        except ValueError:
            print(f'Fila {n_fila}: No puede interpretar: {fila}')
    
    file.close()
    return lista

#%%
# ..:EJERCICIO 3.20:..
from collections import Counter

def contar_ejemplares(lista_arboles):
    
    lista_nombres = []    
    for arbol in lista_arboles:
        
        lista_nombres.append(arbol['nombre_com'])
        tenencias = Counter(lista_nombres)
    
    return tenencias


#%%
# ..:EJERCICIO 3.20:..
#Cada una de las siguientes listas contiene un diccionario en cada elemento, a su vez el diccionario contine todos los datos de cada arbol en el parque solicitado
listaGP = leer_parque('../Data/arbolado-en-espacios-verdes.csv', 'GENERAL PAZ')

cant_espGP = contar_ejemplares(listaGP) #GENERAL PAZ


mas_frecuentesGP = cant_espGP.most_common(5)

print(f'\x1b[1;35m {"..:GENERAL PAZ:..":_^36} \x1b[0m') # \x1b[1;35m Son codigos de color
print(f'\x1b[1;34m {"Nombre":^22} | {"Cantidad":^10} \x1b[0m')

for datos in mas_frecuentesGP:#mas_drecuentes es una lista de tuplas
    nombre, cant = datos
    print(f' {nombre:^22} | {cant:^10}')




