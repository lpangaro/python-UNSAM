#esfera.py

#Author: Lucas Pangaro
#Mail: Pangaro.lucas@gmail.com
#Date: 10/3/21

# ..:ENUNCIADO 1.13:..
#En tu directorio de trabajo de esta clase, escribí un programa llamado esfera.py que le pida al usuario que ingrese por teclado
# el radio r de una esfera y calcule e imprima el volumen de la misma. Sugerencia: recordar que el volúmen de una esfera es 4/3 πr^3.
pi = 3.141592654

print('\nHola! este es el programa para calcular el volumen de una esfera.')
radio = input('Por favor ingrese el radio de la esfera: ')

volumen = (4/3)*pi*(float (radio)**3)
print('Aguarde un instante, estamos procesando los datos...\nEl volumen de una esfera de radio', radio,'es de', round(volumen, 3))


'''
Output:
Hola! este es el programa para calcular el volumen de una esfera.
Por favor ingrese el radio de la esfera: 6
Aguarde un instante, estamos procesando los datos...
El volumen de una esfera de radio 6 es de 904.779
'''