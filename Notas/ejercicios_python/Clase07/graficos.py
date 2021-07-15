#Author: Lucas Pangaro
#Mail: Pangaro.lucas@gmail.com
#Date: 28/04/21

import matplotlib.pyplot as plt

fig = plt.figure()
plt.subplot(2, 1, 1) # define la figura de arriba
plt.plot([0,1,2],[0,1,0]) # dibuja la curva
plt.xticks([]), plt.yticks([]) # saca las marcas

plt.subplot(2, 3, 4) # define la primera de abajo
plt.plot([0,1],[0,1])
plt.xticks([]), plt.yticks([])

plt.subplot(2, 3, 5) # define la segunda de abajo
plt.plot([0,1],[0,0])
plt.xticks([]), plt.yticks([])


plt.subplot(2, 3, 6) # define la segunda de abajo
plt.plot([0,1],[1,0])
plt.xticks([]), plt.yticks([])

plt.show()