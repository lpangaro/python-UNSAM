
#%%
import random

def tirar ():
    tirada = []
    for i in range(5):
        tirada.append( random.randint(1,6) )
    return tirada

def es_generala(tirada):
    
    if len(set(tirada)) != 1: #en el set no puede haber dos valores repetido por lo que si len es mayor a 1 quiere decir que no hubo generala servida
        return False
    return True


N = 1000000
G = sum([es_generala(tirar()) for i in range(N)])
prob = G/N
print(f'Tiré {N} veces, de las cuales {G} saqué generala servida.')
print(f'Podemos estimar la probabilidad de sacar generala servida mediante {prob:.6f}.')

#%%
import random
#random.seed(31415)

tirada=[]
for i in range(5):
    tirada.append(random.randint(1,6)) 

print(tirada)

caras = ['uno', 'dos', 'tres', 'cuatro', 'cinco', 'seis']
print(random.choice(caras))

#%%
import numpy as np
a = np.array([1, 2, 3])
np.empty(2)
