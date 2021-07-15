#informe.py

#Author: Lucas Pangaro
#Mail: Pangaro.lucas@gmail.com

# import informe
# informe.informe_camion('../Data/camion.csv', '../Data/precios.csv')

# ..:EJERCICIO 9.8:..
from fileparse import parse_csv
import lote
import formato_tabla
#%%
def leer_precios(archivo):
    '''Creo un diccionario con los productos y precios de venta del negocio'''
    
    with open (archivo, 'rt') as file:
        precios = parse_csv(file, types=[str,float], has_headers=False)
    
        #"precios" es una lista de tuplas
        d = {}
        for tupla in precios:
            d[tupla[0]] = tupla[1]
    
    return d


def leer_camion(archivo):
    '''
    lee un archivo con el contenido de un camion y devuelva 
    una lista de instancias de Lote
    '''
    with open (archivo, 'rt') as file:
        dic_camion = parse_csv(file, select = ['nombre', 'cajones', 'precio'], types = [str, int, float])

    camion = [ lote.Lote(d['nombre'], d['cajones'], d['precio']) for d in dic_camion]
    
    
    return camion


def hacer_informe(camion, dic_precios):
    lista_de_tuplas = []
    cambio = 0.0
    for s in camion:
        cambio = dic_precios[s.nombre] - s.precio
        tupla = (s.nombre, s.cajones, s.precio, cambio)
        lista_de_tuplas.append(tupla)
  
    return lista_de_tuplas


def imprimir_informe(data_informe, formateador):
  
    formateador.encabezado(['Nombre', 'Cantidad', 'Precio', 'Cambio'])
    for nombre, cajones, precio, cambio in data_informe:
        rowdata = [ nombre, str(cajones), f'{precio:0.2f}', f'{cambio:0.2f}' ]
        formateador.fila(rowdata)


def informe_camion(archivo_camion, archivo_precios, fmt = 'txt'):
    '''
    Crea un informe con la carga de un camión
    a partir de archivos camion y precio.
    El formato predeterminado de la salida es .txt
    Alternativas: .csv o .html
    '''
    # Lee archivos de datos
    camion = leer_camion(archivo_camion)
    precios = leer_precios(archivo_precios)

    # Crea la data del informe
    data_informe = hacer_informe(camion, precios)

    # Imprime el informe
    formateador = formato_tabla.crear_formateador(fmt)
    imprimir_informe(data_informe, formateador)

    
#%%
def main(args):
    if len(args) == 4:
        informe_camion(args[1], args[2], args[3])
    elif len(args) == 3:
        informe_camion(args[1], args[2])
    else:
        raise SystemExit('Uso: %s archivo_camion archivo_precios formato' % args[0])
    
#%%
if __name__ == '__main__':
    import sys
    main(sys.argv)