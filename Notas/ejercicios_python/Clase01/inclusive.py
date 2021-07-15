#inclusive.py

#Author: Lucas Pangaro
#Mail: Pangaro.lucas@gmail.com
#Date: 10/3/21

# ..:ENUNCIADO 1.29:..
#Queremos hacer un traductor que cambie las palabras masculinas de una frase por su versión neutra. 
# Como primera aproximación, completá el siguiente código para reemplazar todas las letras 
# 'o' que figuren en el último o anteúltimo caracter de cada palabra por una 'e'.

frase = 'Los hermanos sean unidos porque ésa es la ley primera'
frase_t = ''

print("\nFrase original: ", frase)

palabras = frase.split()
for palabra in palabras:
    if palabra[-2] == 'o':
        frase_t = frase_t + " " + palabra.replace('o', 'e')

    elif palabra[-1] == 'o':
    	frase_t = frase_t + " " +palabra.replace('o', 'e')

    else:
        frase_t = frase_t + " " +palabra

print("Frase Nueva:", frase_t)


'''
Output:
Frase original:  Los hermanos sean unidos porque ésa es la ley primera
Frase Nueva:  Les hermanes sean unides porque ésa es la ley primera
'''