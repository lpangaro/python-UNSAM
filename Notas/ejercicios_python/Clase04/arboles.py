#arboles.py

#Author: Lucas Pangaro
#Mail: Pangaro.lucas@gmail.com
#Date: 3/4/21

# ..: EJERCICIO 4.18 :..
import csv
def leer_parque (archivo):
    
    file = open (archivo, encoding="utf8")
    lista = []
    filas = csv.reader(file)
    header = next (filas)
    
    for n_fila, fila in enumerate(filas,start=1):
        
        record = dict( zip(header, fila) ) 
        lista.append(record)
     
    file.close()
    return lista


arboleda = leer_parque('../Data/arbolado-en-espacios-verdes.csv')

# ..: EJERCICIO 4.19 :..
H=[float(arbol['altura_tot']) for arbol in arboleda if arbol['nombre_com'] == 'Jacarandá']

# ..: EJERCICIO 4.20 :..
HyD = [ (float(arbol['altura_tot']), float(arbol['diametro'])) for arbol in arboleda if arbol['nombre_com'] == 'Jacarandá']
