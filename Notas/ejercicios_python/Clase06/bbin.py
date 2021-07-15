#bbin.py

#Author: Lucas Pangaro
#Mail: Pangaro.lucas@gmail.com
#Date: 21/04/21

#%% ..:EJERCICIO 6.14:..
def donde_insertar(lista, x):
    '''Búsqueda binaria
    Precondición: la lista está ordenada
    Devuelve la posicion deonde se encuntra el elemento o bien donde se podria agregar para no romper el orden
    '''
    pos = -1
    izq = 0
    der = len(lista) - 1

    while izq <= der:
        medio = (izq + der) // 2
        
        if lista[medio] == x:
            pos = medio
            break     # elemento encontrado! rompe el ciclo y se va
        if lista[medio] > x:
            der = medio - 1 # descarto mitad derecha
        else:               # if lista[medio] < x:
            izq = medio + 1 # descarto mitad izquierda
            
    if pos == -1: #en el caso que el valor no este en la lista
        pos = izq
    return pos

#%% ..:EJERCICIO 6.15:..
def insertar(lista, x):
    
   posicion = donde_insertar(lista,x)

   lista.insert((posicion), x)
      
   print("El elemento fue agregado correctamente")
      
   return posicion
   
#%%
lista = [0,1,2,3,5,6,7,8,10,11]
print (lista)
posicion = insertar(lista, 4)
print (lista)





