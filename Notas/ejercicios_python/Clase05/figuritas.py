#Author: Lucas Pangaro
#Mail: Pangaro.lucas@gmail.com
#Date: 12/4/21
#%%
# ..: EJERCICIO 5.14 :..
import random
import numpy as np

def crear_album(figus_total):
    album = np.zeros(figus_total)

    return album

def album_inclompleto(A):
    valor_de_verdad = False
    if 0 in A:
        valor_de_verdad = True
        
    return valor_de_verdad

def comprar_figu(figus_total):
    num_figu = random.randint(0, figus_total-1)
    return num_figu

def cuantas_figus(figus_total):
    cant = 0
    album = crear_album(figus_total)
    
    while album_inclompleto(album) == True:
        num_figu = comprar_figu(figus_total)
        album[num_figu] = 1
        
        cant += 1
    return cant
    
#%%
figus_total = 670
n = 1000
lista = []
for i in range(n):
    lista.append(cuantas_figus(figus_total))

promedio = np.mean(lista)

'''promedio = 4746'''