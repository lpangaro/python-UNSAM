# -*- coding: utf-8 -*-
#busqueda_en_listas.py

#Author: Lucas Pangaro
#Mail: Pangaro.lucas@gmail.com
#Date: 3/4/21

# ..: EJERCICIO 4.8 :..

def propagar (lista):
    
    l = []  #lista auxiliar
    l2 = [] #lista de retorno
    
    for e in lista:
        if e != -1: #mientras el elemento de la lista no sea un -1 los voy agregando a mi lista auxiliar
            l.append(e)
        else:#cuando el elemento vale -1 tengo un bloque que analizar
            if 1 in l:# si dentro del bloque hay un fosforo encendido (1) propagara el fuego a los otros
                for i in range(len(l)):
                    l[i] = 1
            l2 += l
            
            l2.append(-1)
            l = []
            
    if 1 in l:
        for i in range(len(l)):
            l[i] = 1
    l2 += l
    return l2

lista = [0, 1, 0, 1, 0, 0]
lp = propagar(lista)
