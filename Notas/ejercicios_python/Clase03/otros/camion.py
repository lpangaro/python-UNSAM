# -*- coding: utf-8 -*-
import csv
def costo_camion(archivo):
    costo_total = 0
    f = open (archivo, 'rt')
    filas = csv.reader(f)
    encabezado = next(filas)
    
    for n_fila, fila in enumerate(filas,start=1):
        record = dict(zip(encabezado,fila)) 
        try:
            ncajones = int(record['cajones'])
            precio = float(record['precio'])
            
            costo_total += ncajones * precio
        except ValueError:
            print(f'Fila {n_fila}: No puede interpretar: {fila}')
    
    f.close()
    return(costo_total)


costo = costo_camion('../data/fecha_camion.csv')
print('Costo TOATAL:', costo)