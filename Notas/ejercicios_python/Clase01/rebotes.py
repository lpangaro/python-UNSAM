# rebotes.py

#ENUNCIADO
# Una pelota de goma es arrojada desde una altura de 100 metros y cada vez que toca el piso salta 3/5
# de la altura desde la que cayó. Escribí un programa rebotes.py que imprima una tabla mostrando las 
# alturas que alcanza en cada uno de sus primeros diez rebotes.

#Author: Lucas Pangaro
#Mail: Pangaro.lucas@gmail.com
#Date: 10/3/21

cant_rebotes = 10
altura = 100
factor_rebote = (3/5)

i = 0
while i < cant_rebotes:

    altura = altura * factor_rebote
    print(i+1 , "->", round(altura, 4) )
    
    i = i + 1

'''
Output:
1 -> 60.0
2 -> 36.0
3 -> 21.6
4 -> 12.96
5 -> 7.776
6 -> 4.6656
7 -> 2.7994
8 -> 1.6796
9 -> 1.0078
10 -> 0.6047
'''