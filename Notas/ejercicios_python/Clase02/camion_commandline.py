#camion_commandline.py

#Author: Lucas Pangaro
#Mail: Pangaro.lucas@gmail.com
#Date: 20/3/21

# ..:EJERCICIO 2.10:..
'''Copiá el contenido de costo_camion.py a un nuevo archivo llamado camion_commandline.py que incorpore la lectura de parámetros por línea de comando '''

import csv
import sys

def costo_camion(archivo):
	total = 0
	with open (archivo, 'rt') as f:
		renglones = csv.reader(f)
		headers = next(renglones)

		for row in renglones:
			 total += float(row[1]) * float(row[2])

	return (total)

if len (sys.argv) == 2:
	archivo = sys.argv[1]
else:
	archivo = '../data/camion.csv'

costo = costo_camion(archivo)
print('Costo Total:', costo)


'''
Output
>>>camion_commandline.py
Costo Total: 47671.15

>>>camion_commandline.py ../data/camion.csv
Costo Total: 47671.15
'''