#Author: Lucas Pangaro
#Mail: Pangaro.lucas@gmail.com
#Date: 12/4/21
#%%
# ..: EJERCICIO 5.7 :..
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