#documentacion.py

#Author: Lucas Pangaro
#Mail: Pangaro.lucas@gmail.com
#Date: 28/04/21
#%%
def valor_absoluto(n):
    '''Calcula el modulo de un numero
    
    Pre: n es un numero real
    Pos: Devulve "n" si "n" es positivo y "-n" si "n" es negativo
    '''
    if n >= 0:
        return n
    else:
        return -n
    
#%%
def suma_pares(l):
    ''' Calcula la suma de numeros pares en una lista, 
    si no hay numeros pares devulve 0
    
    Pre: l es una lista de numeros
    Pos: devulve la suma de los numeros pares 
    '''
        
    res = 0
    for e in l:
        if e % 2 ==0:
            res += e
        else:
            res += 0

    return res
#res es inmutable, siempre almacena la suma de numer pares

#%%
def veces(a, b):
    '''Calcula el producto entre dos numeros
    
    Pre: a es un float y b un entero mayor o iguala 0
    Pos: res es la suma de "a" veces "b"
    '''
    res = 0
    nb = b
    while nb != 0:
        #print(nb * a + res)
        res += a
        nb -= 1
    return res

#%%
def collatz(n):
    ''' Collatz: si el nuemero es par lo divide entre 2.
    Si es impar, lo multipmlica por 3 y le suma 1.
    Al resultado se le vulve a aplicar el algoritmo.
    
    
    Pre: n cualquier numero mayor a 0
    Pos: devulve la cantidad de operaciones que se realizan hasta 
    llegar a 1 al aplicar la conjetura de Collatz a "n"'''
    
    res = 1

    while n!=1:
        if n % 2 == 0: #n par
            n = n//2
        else: #n impar
            n = 3 * n + 1
        res += 1

    return res
