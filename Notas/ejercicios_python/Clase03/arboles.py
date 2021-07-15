# -*- coding: utf-8 -*-
#arboles.py

#Author: Lucas Pangaro
#Mail: Pangaro.lucas@gmail.com
#Date: 27/3/21

#%%
'''***************** FUNCIONES *****************'''
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


lista = leer_parque('../Data/arbolado-en-espacios-verdes.csv', 'INDOAMERICANO')

#%%
# ..:EJERCICIO 3.19:..
def especies(lista_arboles):
    lista = []
    for arbol in lista_arboles:
        
        lista.append(arbol['nombre_com']) #Creo una lista con todos los nombres (repetidos)
        conjunto = set(lista) #limpio los duplicados
        
    return conjunto
    
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
# ..:EJERCICIO 3.21:..
def obtener_alturas(lista_arboles, especie):
    
    lista_alturas = []
    altura = 0.0
    
    for arbol in lista_arboles:
        if especie == arbol['nombre_com']:
            altura = float(arbol['altura_tot'])
            lista_alturas.append(altura)
    
    return lista_alturas

#%%
# ..:EJERCICIO 3.22:..
def obtener_inclinaciones(lista_arboles, especie):
    
    lista_inclinacion = []
    inclinacion = 0
    
    for arbol in lista_arboles:
        if especie == arbol['nombre_com']:
            inclinacion = int(arbol['inclinacio'])
            lista_inclinacion.append(inclinacion)
    
    return lista_inclinacion

#%%
# ..:EJERCICIO 3.23:..
def especimen_mas_inclinado(lista_arboles):
    
    list_especie = especies(lista_arboles)
    
    mas_inclinado = 0
    
    for especie in list_especie:
        inclinacion = max( obtener_inclinaciones(lista_arboles, especie) ) #de la lista de arboles de esa especie me quedo con el mas inclinado
        
        if inclinacion > mas_inclinado:
            mas_inclinado = inclinacion
            especie_mas_inclinada = especie
    
    return especie_mas_inclinada, mas_inclinado

#%%
# ..:EJERCICIO 3.24:..'

def especie_promedio_mas_inclinada(lista_arboles):
    
    list_especie = especies(lista_arboles)
    
    mayor_incl_prom = 0
    
    for especie in list_especie:
        suma_inclinaciones = sum(obtener_inclinaciones(lista_arboles, especie))
        
        cantidad_arboles = len(obtener_inclinaciones(lista_arboles, especie))
        promedio = suma_inclinaciones / cantidad_arboles
        
        if promedio > mayor_incl_prom:
            mayor_incl_prom = promedio
            especie_prom_inclinada = especie
            
    return especie_prom_inclinada, mayor_incl_prom


#%%
'''***************** PRINTS Y LLAMADOS A FUNCIONES *****************'''
#%%
# ..:EJERCICIO 3.18:..
lista = leer_parque('../Data/arbolado-en-espacios-verdes.csv', 'GENERAL PAZ')
#print(len(lista)) #690

#%%
# ..:EJERCICIO 3.19:..
conjunto_especies = especies (lista)
#print(conjunto_especies)

#%%
# ..:EJERCICIO 3.20:..
#Cada una de las siguientes listas contiene un diccionario en cada elemento, a su vez el diccionario contine todos los datos de cada arbol en el parque solicitado
listaGP = leer_parque('../Data/arbolado-en-espacios-verdes.csv', 'GENERAL PAZ')
listaLA = leer_parque('../Data/arbolado-en-espacios-verdes.csv', 'ANDES, LOS')
listaC = leer_parque('../Data/arbolado-en-espacios-verdes.csv', 'CENTENARIO')

#las siguientes funciones devulven Counter's con las especies de cada parque y su cantidad
cant_espGP = contar_ejemplares(listaGP) #GENERAL PAZ
cant_espLA = contar_ejemplares(listaLA) #LOS ANDES
cant_espC = contar_ejemplares(listaC) #CENTENARIO

#Creo listas con las 5 especies mas frecunetes
mas_frecuentesGP = cant_espGP.most_common(5)
mas_frecuentesLA = cant_espLA.most_common(5) 
mas_frecuentesC = cant_espC.most_common(5)
'''
print(f'\x1b[1;34m {"..:GENERAL PAZ:..":_^31} \x1b[1;35m{"..:LOS ANDES:..":_^31} \x1b[1;32m{"..:CENTENARIO:..":_^31} \x1b[0m') #\x1b[1;34m SON CODIGOS DE COLOR
for index in range(5):
    name_GP, cant_GP = mas_frecuentesGP[index]
    name_LA, cant_LA = mas_frecuentesLA[index]
    name_C, cant_C = mas_frecuentesC[index]
    
    print(f'| {name_GP:<23}: {cant_GP:<4} | {name_LA:<23}: {cant_LA:<4} | {name_C:<23}: {cant_C:<4} |')
'''
#%%
# ..:EJERCICIO 3.21:..
especie = 'Jacarandá'
altura_GP = obtener_alturas(listaGP, especie)
altura_LA = obtener_alturas(listaLA, especie)
altura_C = obtener_alturas(listaC, especie)
'''
print(f'\n..:GENERAL PAZ:..\nLa altura maxima del {especie} es de {max(altura_GP)}')
print(f'La altura promedio del {especie} es de {(sum(altura_GP)/len(altura_GP)):.4}')

print(f'\n..:LOS ANDES:..\nLa altura maxima del {especie} es de {max(altura_LA)}')
print(f'La altura promedio del {especie} es de {(sum(altura_LA)/len(altura_LA)):.4}')

print(f'\n..:CENTENARIO:..\nLa altura maxima del {especie} es de {max(altura_C)}')
print(f'La altura promedio del {especie} es de {(sum(altura_C)/len(altura_C)):.4}')
'''

#%%
# ..:EJERCICIO 3.23:..
especie , inclinacion = especimen_mas_inclinado(listaC) #lista de arboles del centenario
#print(f'Los {especie} con una inclinacion de {inclinacion}º es el especimen mas inclinado')

#%%
# ..:EJERCICIO 3.24:..
especie_prom, inclinacion_prom = especie_promedio_mas_inclinada(listaLA)
#print(f'Los {especie_prom} tienen un promedio de inclinacion de {inclinacion_prom}º')

