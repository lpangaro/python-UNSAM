#burbujeo.py

#Author: Lucas Pangaro
#Mail: Pangaro.lucas@gmail.com
#Date: 16/6/21

#%%
def ord_burbujeo(lista):
    comparaciones = 0
    for n in range(len(lista)-1 , 0, -1):
        
        for i in range(n):
            if lista[i] > lista[i+1]:
                lista[i], lista[i+1] = lista[i+1], lista[i]
            comparaciones += 1
            
    print('comparaciones: ', comparaciones)
    
    
    
#%%    
lista_1 = [1, 2, -3, 8, 1, 5]

print(lista_1)
ord_burbujeo(lista_1)
print(lista_1)

#%%
lista_2 = [1, 2, 3, 4, 5]
lista_3 = [0, 9, 3, 8, 5, 3, 2, 4]
lista_4 = [10, 8, 6, 2, -2, -5]
lista_5 = [2, 5, 1, 0]
