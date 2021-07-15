#diccionario_geringoso.py

#Author: Lucas Pangaro
#Mail: Pangaro.lucas@gmail.com
#Date: 20/3/21

def geringoso(palabra):
    palabra_Nueva = ""

    for c in palabra:
        palabra_Nueva += c
        if c in "aeiou":
            palabra_Nueva += 'p' + c
    return(palabra_Nueva)


lista = ['banana', 'manzana', 'mandarina', 'melon', 'anana', 'kiwi']
d = {} #creo un diccionario vacio

for palabra in lista:
    d[palabra] = geringoso(palabra) #agrego al diccionario

#imprimo el diccionario 
for k in d:
    print(k, '=', d[k])

'''
Output
banana = bapanapanapa
manzana = mapanzapanapa
mandarina = mapandaparipinapa
melon = mepelopon
anana = apanapanapa
kiwi = kipiwipi
'''