#tablamult.py

#Author: Lucas Pangaro
#Mail: Pangaro.lucas@gmail.com
#Date: 25/3/21

# ..:EJERCICIO 3.17:..
'''
Escribí un programa tablamult.py que imprima de forma prolija las tablas 
de multiplicar del 1 al 9 usando f-strings. Si podés, evitá usar la multiplicación, 
usando sólo sumas alcanza.
'''

header= '     0   1   2   3   4   5   6   7   8   9'
print('\n\x1b[1;34m'+header)     #\x1b[1;34m ES UN CODIGO DE COLOR
print(f'{"":_>44} \n') #linea horizontal

for tabla in range(10): #filas
    print(f'\x1b[1;34m {tabla}:\x1b[0m', end ='') #imprimo los indices
    
    j = 0
    for cont in range(10): #columnas
        print(f'{j:>3}', end=' ')
        j = j + tabla
    
    print('\n')
     
    
'''
     0   1   2   3   4   5   6   7   8   9
____________________________________________ 

 0:  0   0   0   0   0   0   0   0   0   0 

 1:  0   1   2   3   4   5   6   7   8   9 

 2:  0   2   4   6   8  10  12  14  16  18 

 3:  0   3   6   9  12  15  18  21  24  27 

 4:  0   4   8  12  16  20  24  28  32  36 

 5:  0   5  10  15  20  25  30  35  40  45 

 6:  0   6  12  18  24  30  36  42  48  54 

 7:  0   7  14  21  28  35  42  49  56  63 

 8:  0   8  16  24  32  40  48  56  64  72 

 9:  0   9  18  27  36  45  54  63  72  81 
'''
    
    
    
    