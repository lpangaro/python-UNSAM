#%%
def my_busqueda (lista, e):
    aux = -1
    for i in range(len(lista)):
        if lista[i] == e:
            aux = i
    return aux

#%%
def busqueda_lineal(lista, e):

    pos = -1  # comenzamos suponiendo que e no está
    for i, z in enumerate(lista): # recorremos la lista
        if z == e:   # si encontramos a e
            pos = i  # guardamos su posición
            break    # y salimos del ciclo
    return pos
#%%
lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
e = 5
indicie = busqueda_lineal(lista, e)
print(indicie)
# %%
