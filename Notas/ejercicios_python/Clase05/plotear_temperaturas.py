#Author: Lucas Pangaro
#Mail: Pangaro.lucas@gmail.com
#Date: 12/4/21
#%%
# ..: EJERCICIO 5.8 :..
import numpy as np
import matplotlib.pyplot as plt

vector = np.load('../Data/Temperaturas.npy') #cargo los datos

plt.hist (vector,bins=25)
