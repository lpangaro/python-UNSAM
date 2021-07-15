#Author: Lucas Pangaro
#Mail: Pangaro.lucas@gmail.com
#Date: 12/4/21
#%%
# ..: EJERCICIO 5.2 :..
import random

def multiples_tiradas():
    '''Devuelve True o False, segun si en las 3 tiradas se consiguio generala o no'''
    tirada = []
    cont = 0
    mas_veces = 0

    '''PRIMER TIRADA'''
    for i in range(5):
            tirada.append( random.randint(1,6) )
    #print(tirada)

    '''Analizo que numero sale mas veces y que cantidad'''
    for i in range(1,7):
        for e in tirada:
            if i == e:
                cont += 1

        if mas_veces < cont:
            mas_veces = cont
            numero = i

        cont = 0

    '''SEGUNDA TIRADA'''
    for i in range(5-mas_veces):
        if random.randint(1,6) == numero:
            mas_veces += 1 
            #print (numero)


    '''TERCER TIRADA'''
    for i in range(5-mas_veces):
        if random.randint(1,6) == numero:
            mas_veces += 1 
            #print (numero)

    if mas_veces == 5: #Si es generala retorna Verdadero
        return True

    return False

N = 100000
G = sum(multiples_tiradas() for i in range(N))
prob = G/N

print(f'Tiré {N} veces, de las cuales {G} saqué generala.')
print(f'Podemos estimar la probabilidad de sacar generala mediante {prob:.6f}.')