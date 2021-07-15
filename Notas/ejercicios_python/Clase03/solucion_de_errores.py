# -*- coding: utf-8 -*-
"""
Created on Wed Mar 24 15:33:51 2021

@author: panga
"""
#%%
# ..:Ejercicio 3.1  Función tiene_a():..
'''Comentario: habia dos errores principalmente. el primero y mas importante era que la 
funcion evaluava unicamentet el primer caracter debidodo a que estaba el return dentro
del if - else.

para corregirlo creé una variable booleana inicializada en falso
que cambiaria su estado unicamente al entrar el if; ademas saque los return de las condiciones y deje
un unico return al final del programa. de esta forma el while recorrera toda la cadena '''

'''El segundo problema era que no tenia en cuenta A Á á.
para resolver esto simplemente cambie la condicion de == por in con la cadena 'aAáÁ'
'''

def tiene_a(expresion):
    n = len(expresion)
    i = 0
    aux = False
    while i < n:
        if expresion[i] in 'aAáÁ':
            aux = True
        else:
            pass
        i += 1
    return aux    

print( tiene_a('UNSAM 2020') )
print( tiene_a('abracadabra') )
print( tiene_a('La novela 1984 de George Orwell') )

'''
True
True
True
'''