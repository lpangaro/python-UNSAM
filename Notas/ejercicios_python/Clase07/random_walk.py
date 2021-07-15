import numpy as np
import matplotlib.pyplot as plt

def randomwalk(largo):
    pasos = np.random.randint(-1,2,largo)    
    return pasos.cumsum()

N = 100000

#creo condiciones iniciales con un primer pasos
inicio_pasos = randomwalk(N)
valor = max(abs(inicio_pasos.cumsum()))
alejado = inicio_pasos
cercano = inicio_pasos

plt.subplot(2,1,1)
plt.plot(inicio_pasos)

for i in range (11): 
    
    pasos = randomwalk(N)
    
    #Evaluo respecto de la primer inicio_pasos o bien sobre el valor minimo o maximo
    if max(abs(pasos.cumsum())) > valor:
        alejado = pasos
        valor = max(abs(pasos.cumsum()))
    
    if max(abs(pasos.cumsum())) < valor:
        cercano = pasos
        valor = max(abs(pasos.cumsum()))
        
    plt.subplot(2,1,1)
    plt.plot(pasos)
    plt.title("12 Caminatas al azar")
    plt.xticks([])
    
    
    #plt.xlabel("Distancia al origen")
    #plt.ylabel("Tiempo")


plt.subplot(2,2,3)
plt.plot(alejado)
plt.title("La caminata que mas se aleja")
plt.xticks([])


plt.subplot(2,2,4)
plt.plot(cercano)
plt.title("La caminata que menos se aleja")
plt.xticks([])

    
