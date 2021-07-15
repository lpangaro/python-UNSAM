#Author: Lucas Pangaro
#Mail: Pangaro.lucas@gmail.com
#Date: 12/4/21
#%%..: EJERCICIO 5.5 :..
'''
import random
mu = 0
sigma = 0.2
n = 99
lista = []
for i in range(n):

    temperatura = 37.5 + random.normalvariate(mu, sigma)
    lista.append(round (temperatura,2))

print(f'TEMPERATURAS...\n{lista}')
print(f'\x1b[1;35m MAXIMO: {max(lista)}')
print(f'\x1b[1;34m MINIMO: {min(lista)}')
print(f'\x1b[1;32m PROMEDIO: {sum(lista)/n:.2f}')

lista_ordenada = sorted(lista) #ordena la lista
n = int ((n-1) / 2)
print(f'\x1b[1;31m MEDIANA: {lista_ordenada[n]}')
'''
#%%..: EJERCICIO 5.7 :..

import numpy as np
import random
mu = 0
sigma = 0.2
n = 999
lista = []
for i in range(n):

    temperatura = 37.5 + random.normalvariate(mu, sigma)
    lista.append(round (temperatura,2))

vector = np.array(lista)
np.save('../Data/Temperaturas.npy',vector)