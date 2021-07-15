#precios.py

#Author: Lucas Pangaro
#Mail: Pangaro.lucas@gmail.com
#Date: 20/3/21

# ..:EJERCICIO 2.3:..
# Escribí un código que abra el archivo Data/precios.csv, busque el precio de la naranja y lo imprima en pantalla.
'''
with open ("precios.csv", "rt") as f:
    for line in f:
        if 'Naranja' in line:
            row = line.split(',')
            print('El precio de la Naranja es:', row[1])
'''

# ..:EJERCICIO 2.7:..
'''
A partir de lo que hiciste en el Ejercicio 2.3, escribí una función buscar_precio(fruta) 
que busque en archivo ../Data/precios.csv el precio de determinada fruta (o verdura) 
y lo imprima en pantalla. Si la fruta no figura en el listado de precios, 
debe imprimir un mensaje que lo indique.
'''
 
def buscar_precio(nombre_fruta):
    aux = -1
    with open ("../Data/precios.csv", "rt") as f:
        for line in f:
            if nombre_fruta in line:
                row = line.split(',')
                aux = float(row[1])

    return (aux)
    

fruta = input ('ingrese el nombre de la fruta de la que quiere conocer su precio: ')
precio = buscar_precio(fruta)

if precio > 0:
    print (f'El precio de {fruta} es {precio}')

else:
    print(f'{fruta} no figura en el listado de precios')

'''
Output
El precio de Naranja es 106.28

Melon no figura en el listado de precios
'''