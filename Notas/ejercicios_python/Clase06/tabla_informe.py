#informe_funciones.py

#Author: Lucas Pangaro
#Mail: Pangaro.lucas@gmail.com
#Date: 18/04/21


# ..:EJERCICIO 6.11:..
from fileparse import parse_csv
#%%
def leer_precios(archivo):
    '''Creo un diccionario con los productos y precios de venta del negocio'''
    
    precios = parse_csv('../Data/precios.csv', types=[str,float], has_headers=False)
    #"precios" es una lista de tuplas
    d = {}
    for tupla in precios:
        d[tupla[0]] = tupla[1]
    
    return d

#%%
def leer_camion(archivo):
    '''Creo una lista de diccionarios, cada elemento de la lista contiene un diccionaria con nombre, cajones y precio'''
    
    camion = parse_csv('../Data/camion.csv', select = ['nombre', 'cajones', 'precio'], types = [str, int, float])

    return camion

#%%
def hacer_informe(camion, dic_precios):
    lista_de_tuplas = []
    cambio = 0.0
    for s in camion:
        cambio = dic_precios[s['nombre']] - s['precio']
        tupla = (s['nombre'], s['cajones'], s['precio'], cambio)
        lista_de_tuplas.append(tupla)
  
    return lista_de_tuplas

#%%
camion = leer_camion('../data/camion.csv')
dic_precios = leer_precios('../Data/precios.csv')

informe = hacer_informe(camion, dic_precios)

#%% prints
headers = ('Nombre', 'Cajones', 'Precio', 'Cambio')

print (f'\x1b[1;35m {headers[0]:>10s} {headers[1]:>10s} {headers[2]:>10s} {headers[3]:>10s}') #\x1b[1;35m  codigo de color
print(f' {"":->44} \x1b[0m') #linea horizontal


for nombre, cajones, precio, cambio in informe:
    str_precio = '$'+ str(precio)
    print(f'{nombre:>10s} {cajones:>10d}  {str_precio:>10s} {cambio:>10.2f}')

           














