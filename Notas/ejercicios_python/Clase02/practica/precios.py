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

print ('*************LISTA DE PRECIOS*****************')
precios = leer_precios('../Data/precios.csv')

print(precios['Naranja']) #asi accedo al precio de la naranja

'''
from pprint import pprint
pprint(precios)
'''