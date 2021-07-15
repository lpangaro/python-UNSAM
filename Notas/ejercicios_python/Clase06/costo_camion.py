#costo_camion.py

#Author: Lucas Pangaro
#Mail: Pangaro.lucas@gmail.com
#Date: 21/04/21

# ..:EJERCICIO 6.12:..

from informe_funciones import leer_camion
def costo_camion(archivo):
    '''mediante la funcion leer_camion importada de "informe_funciones" calcula el costo de un camion'''
    total = 0
    camion = leer_camion(archivo)
    
    for producto in camion:
        total += producto['cajones'] * producto['precio']   
    
    return(total)

costo = costo_camion('../Data/camion.csv')
print('\n\x1b[1;33mCosto TOATAL:', costo)

'''
     Nombre    Cajones     Precio     Cambio
 -------------------------------------------- 
      Lima        100       $32.2       8.02
   Naranja         50       $91.1      15.18
     Caqui        150     $103.44       2.02
 Mandarina        200      $51.23      29.66
   Durazno         95      $40.37      33.11
 Mandarina         50       $65.1      15.79
   Naranja        100      $70.44      35.84
   
Costo TOATAL: 47671.15
'''