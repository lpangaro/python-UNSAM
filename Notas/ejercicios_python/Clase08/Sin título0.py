import numpy as np

mat = np.array([[1,0,0], [4,0,6],[7,0,9]])
n =3
suma = 0 
for i in range (n):
    for j in range (n):
        if mat [i][j] == 0:
            suma +=1
            
suma = n*n - suma