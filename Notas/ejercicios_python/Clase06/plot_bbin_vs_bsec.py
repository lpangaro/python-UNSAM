#plot_bbin_vs_bsec.py

#Author: Lucas Pangaro
#Mail: Pangaro.lucas@gmail.com
#Date: 21/04/21

# ..:EJERCICIO 6.20:..

import matplotlib.pyplot as plt
import numpy as np
import random
#%%
def busqueda_secuencial_(lista, x):
    '''Si x está en la lista devuelve el índice de su primera aparición, 
    de lo contrario devuelve -1. Además devuelve la cantidad de comparaciones
    que hace la función.
    '''
    comps = 0 # inicializo en cero la cantidad de comparaciones
    pos = -1
    for i,z in enumerate(lista):
        comps += 1 # sumo la comparación que estoy por hacer
        if z == x:
            pos = i
            break
    return pos, comps

def busqueda_binaria(lista, x):
    '''Búsqueda binaria
    Precondición: la lista está ordenada
    Devuelve -1 si x no está en lista;
    Devuelve p tal que lista[p] == x, si x está en lista
    '''
    comps = 0
    pos = -1 # Inicializo respuesta, el valor no fue encontrado
    izq = 0
    der = len(lista) - 1
    
    while izq <= der:
        
        medio = (izq + der) // 2
        comps += 1
        if lista[medio] == x:
            pos = medio     # elemento encontrado!
        if lista[medio] > x:
            der = medio - 1 # descarto mitad derecha
        else:               # if lista[medio] < x:
            izq = medio + 1 # descarto mitad izquierda
    return pos, comps
#%%
def generar_lista(n, m):
    l = random.sample(range(m), k = n)
    l.sort()
    return l

def generar_elemento(m):
    return random.randint(0, m-1)

#%%
def experimento_secuencial_promedio(lista, m, k):
    comps_tot = 0
    for i in range(k):
        x = generar_elemento(m)
        comps_tot += busqueda_secuencial_(lista,x)[1]

    comps_prom = comps_tot / k
    return comps_prom

def experimento_binario_promedio(lista, m, k):
    comps_tot = 0
    for i in range(k):
        x = generar_elemento(m)
        comps_tot += busqueda_binaria(lista,x)[1]

    comps_prom = comps_tot / k
    return comps_prom
 
#%%
m = 10000
k = 1000
n = 100
lista = generar_lista(n, m)

# acá comienza el experimento
x = generar_elemento(m)
S_comps = busqueda_secuencial_(lista, x)[1]
B_comps = busqueda_binaria(lista, x)[1]

largos = np.arange(256) + 1 # estos son los largos de listas que voy a usar
comps_sec_promedio = np.zeros(256) # aca guardo el promedio de comparaciones sobre una lista de largo i, para i entre 1 y 256.
comps_bin_promedio = np.zeros(256)

for i, n in enumerate(largos):
    lista = generar_lista(n, m) # genero lista de largo n
    comps_sec_promedio[i] = experimento_secuencial_promedio(lista, m, k)
    comps_bin_promedio[i] = experimento_binario_promedio(lista, m, k)

# ahora grafico largos de listas contra operaciones promedio de búsqueda.
plt.plot(largos, comps_sec_promedio, label = 'Búsqueda Secuencial')
plt.plot(largos, comps_bin_promedio, label = 'Búsqueda Binaria')

plt.xlim(0, 50)
plt.ylim(0, 20)

plt.xlabel("Largo de la lista")
plt.ylabel("Cantidad de comparaciones")
plt.title("Complejidad de la Búsqueda")
plt.legend()
