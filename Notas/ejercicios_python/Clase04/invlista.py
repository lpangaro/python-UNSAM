#invlista.py

#Author: Lucas Pangaro
#Mail: Pangaro.lucas@gmail.com
#Date: 3/4/21

# -*- coding: utf-8 -*-

# ..: EJERCICIO 4.8 :..
def invertir_lista(lista):
    invertida = []
    for e in lista:
        invertida.insert(0, e)
    return invertida

l1 = invertir_lista(['Bogotá', 'Rosario', 'Santiago', 'San Fernando', 'San Miguel'])
print(l1)
l2 = invertir_lista([1, 2, 3, 4, 5])
print(l2)
'''
['San Miguel', 'San Fernando', 'Santiago', 'Rosario', 'Bogotá']
[5, 4, 3, 2, 1]
'''