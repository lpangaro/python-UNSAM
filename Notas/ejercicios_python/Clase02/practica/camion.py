import csv
def leer_camion(archivo):
    '''Creo una lista de diccionarios, cada elemento de la lista contiene un diccionaria con nombre, cajones y precio'''
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

#print(camion) #esto me devuelve toda la lista
#print(camion[0]) #Esto me devuelve el primer diccionario de la lista
print(camion[0]['precio'])#esto devuelve el precio del primer diccionario

'''
for s in camion:
    total += s['cajones']*s['precio']

print ('*************LISTA DE CAMION*****************')
from pprint import pprint
pprint(camion)
'''