# fileparse.py

#Author: Lucas Pangaro
#Mail: Pangaro.lucas@gmail.com
#Date: 21/04/21

#%%..:EJERCICIO 6.8:..
import csv

def parse_csv(nombre_archivo, select = None, types = None, has_headers = True):
    '''
    Parsea un archivo CSV en una lista de registros.
    Se puede seleccionar sólo un subconjunto de las columnas, determinando el parámetro select, que debe ser una lista de nombres de las columnas a considerar.
    '''
    with open(nombre_archivo) as f:
        filas = csv.reader(f)

        if has_headers == True:
            
            # Lee los encabezados del archivo
            encabezados = next(filas)
    
            # Si se indicó un selector de columnas,
            #    buscar los índices de las columnas especificadas.
            # Y en ese caso achicar el conjunto de encabezados para diccionarios
    
            if select:
                indices = [encabezados.index(nombre_columna) for nombre_columna in select]
                encabezados = select
            else:
                indices = []

        registros = []
        for fila in filas:
            if not fila:    # Saltear filas vacías
                continue
            
            # Filtrar la fila si se especificaron columnas
            if (has_headers == True) and (indices):
                fila = [fila[index] for index in indices]
                
            # Asigno tipo de dato correcto si se lo especificaron    
            if types:
                fila = [func(val) for func, val in zip(types, fila)]

            if has_headers == True:
                # Armar el diccionario
                registro = dict(zip(encabezados, fila))
                registros.append(registro)
            else:
                # Arma la tupla
                tupla = (fila[0],fila[1])
                registros.append(tupla)

    return registros


precios = parse_csv('../Data/precios.csv', types=[str,float], has_headers=False)
cajones_lote = parse_csv('../Data/camion.csv', select=['nombre', 'cajones'] , types=[str, int])

