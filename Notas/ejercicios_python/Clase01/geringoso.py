#geringoso.py

#Author: Lucas Pangaro
#Mail: Pangaro.lucas@gmail.com
#Date: 11/3/21

# ..:EJERCICIO 1.18:..
# Usá una iteración sobre el string cadena para agregar la sílaba 'pa', 'pe', 'pi', 'po', o 'pu' según corresponda luego de cada vocal.

cadena = input ('ingrese una palabra": ') #pido la palabra por linea de comandos 
cadena_nueva = ''

for c in cadena:
    if c == 'a':
        cadena_nueva = cadena_nueva + c.replace('a' , 'apa')

    elif c == 'e':
        cadena_nueva = cadena_nueva + c.replace('e', 'epe')

    elif c == 'i':
        cadena_nueva = cadena_nueva + c.replace('i', 'ipi')

    elif c == 'o':
        cadena_nueva = cadena_nueva + c.replace('o', 'opo')

    elif c == 'u':
        cadena_nueva = cadena_nueva + c.replace('u', 'upu')

    else:
        cadena_nueva = cadena_nueva + c
   
print(cadena_nueva)

'''
Output: 
ingrese una palabra": boligoma
bopolipigopomapa
'''

'''
palabra = "Geringoso"
palabra_Nueva = ""

for c in palabra:
    palabra_Nueva += c
    if c in "aeiou":
        palabra_Nueva += 'p' + c
'''