#Author: Lucas Pangaro
#Mail: Pangaro.lucas@gmail.com
#Date: 12/4/21

import os
import matplotlib.pyplot as plt
import csv
def leer_arboles (archivo):
    
    file = open (archivo, encoding="utf8")
    lista = []
    filas = csv.reader(file)
    header = next (filas)
    
    for n_fila, fila in enumerate(filas,start=1):
        
        record = dict( zip(header, fila) ) 
        lista.append(record)
     
    file.close()
    return lista


arboleda = leer_arboles('../Data/arbolado-en-espacios-verdes.csv')

# ..: EJERCICIO 5.24 :..
altos = [float(arbol['altura_tot']) for arbol in arboleda if arbol['nombre_com'] == 'Jacarandá']
plt.figure()
plt.hist(altos,bins=30)

# ..: EJERCICIO 5.25 :..
diametros = [float(arbol['diametro']) for arbol in arboleda if arbol['nombre_com'] == 'Jacarandá']
plt.figure()
plt.xlabel("diametro (cm)")
plt.ylabel("alto (m)")
plt.title("Relación diámetro-alto para Jacarandás")
plt.scatter(diametros, altos)

