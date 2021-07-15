#tablamult.py

#Author: Lucas Pangaro
#Mail: Pangaro.lucas@gmail.com
#Date: 25/3/21

# ..:EJERCICIO 3.17:..
'''
Escribí un programa tablamult.py que imprima de forma prolija las tablas 
de multiplicar del 1 al 9 usando f-strings. Si podés, evitá usar la multiplicación, 
usando sólo sumas alcanza.
'''
#lista = []
#lista_de_listas = []

print(range(10))
for tabla in range(10):
    j = tabla
    #lista = [0] #limpio la lista para cargar la nueva tabla
    print (' 0', end=' ')
    for cont in range(9):
        print(f'{j:>3}', end=' ')
        #lista.append(j)
        j = j+tabla
    
    print('\n')
    '''    
    print('cont=',tabla, end=' ')
    print(f'{lista}')
    '''
    #lista_de_listas.append(lista)
    
    #print (lista)
    
    
    
    
    
    