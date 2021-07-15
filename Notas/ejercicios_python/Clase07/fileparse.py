# fileparse.py

#Author: Lucas Pangaro
#Mail: Pangaro.lucas@gmail.com
#Date: 28/04/21
#%%..:EJERCICIO 7.4:..
import csv
import gzip


def parse_csv(lineas, select = None, types = None, has_headers = True):
    '''
    Parsea un archivo CSV en una lista de registros.
    Se puede seleccionar sólo un subconjunto de las columnas, determinando el parámetro select, que debe ser una lista de nombres de las columnas a considerar.
    '''
    lineas = csv.reader(lineas)
    
    if has_headers == True:
        
        # Lee los encabezados del archivo
        encabezados = next(lineas)

        # Si se indicó un selector de columnas,
        #    buscar los índices de las columnas especificadas.
        # Y en ese caso achicar el conjunto de encabezados para diccionarios

        if select:
            indices = [encabezados.index(nombre_columna) for nombre_columna in select]
            encabezados = select
        else:
            indices = []

    registros = []
    
    for linea in lineas:
        if not linea:    # Saltear lineas vacías
            continue
        
        # Filtrar la linea si se especificaron columnas
        if (has_headers == True) and (indices):
            linea = [linea[index] for index in indices]
            
        # Asigno tipo de dato correcto si se lo especificaron    
        if types:
            linea = [func(val) for func, val in zip(types, linea)]

        if has_headers == True:
            # Armar el diccionario
            registro = dict(zip(encabezados, linea))
            registros.append(registro)
        else:
            # Arma la tupla
            tupla = (linea[0],linea[1])
            registros.append(tupla)

    return registros




with gzip.open('../Data/camion.csv.gz', 'rt') as f:
    
    camion = parse_csv(f, types=[str,int,float])



