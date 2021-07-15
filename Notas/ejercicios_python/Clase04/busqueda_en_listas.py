#busqueda_en_listas.py

#Author: Lucas Pangaro
#Mail: Pangaro.lucas@gmail.com
#Date: 3/4/21
#%% # ..: EJERCICIO 4.6 :..
def buscar_u_elemento(lista, e):
    pos = -1
    for i in range(len(lista)):
        if lista[i] == e:
            pos = i
    return pos

def buscar_n_elemento(lista, e):
    cant = 0
    for elemento in lista:
        if elemento == e:
            cant += 1
    return cant

#%% ..: EJERCICIO 4.7 :..

def maximo(lista):
    m = lista[0]
    for elemento in lista:
        if elemento > m:
            m = elemento
    return m

def minimo(lista):
    m = lista[0]
    for elemento in lista:
        if elemento < m:
            m = elemento
    return m
#%%
'''
buscar_u_elemento([1,2,3,2,3,4],1)
buscar_u_elemento([1,2,3,2,3,4],2)
buscar_u_elemento([1,2,3,2,3,4],3)
buscar_u_elemento([1,2,3,2,3,4],5)

buscar_n_elemento([1,2,3,2,3,4],1)
buscar_n_elemento([1,2,3,2,2,4],2)
buscar_n_elemento([1,2,3,2,3,4],3)
buscar_n_elemento([1,2,3,2,3,4],5)

maximo ([1,2,3,2,10,4])
maximo ([-5, -4])

minimo([-5,2])
minimo ([1,2,3,2,10,4])
'''