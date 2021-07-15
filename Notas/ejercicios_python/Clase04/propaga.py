#propaga.py

#Author: Lucas Pangaro
#Mail: Pangaro.lucas@gmail.com
#Date: 3/4/21
'''
La idea de este programa es tomar la lista 'fosforos' y separarla
en secciones delimitadas por los fosforos quemados (-1). Luego cada 
seccion se analiza para saber si hay un fosforo encendido en dicho 
conjunto o no.
Si en el grupo que estoy mirando hay un 1 todo el grupo se tranforma en 1s
mientras que si son todos 0 se quedan asi
'''
#%%
def propagar (lista):
    
    fosforos = []
    propagada = []
    cont = 0
    
    for e in lista:
        if e != -1: #separo en grupos de fosforos hasta llegar al proximo quemado
            fosforos.append(e)
            
        else: #cunado el fosforo esta quemado analizo el grupo (lista)
            if 1 in fosforos: #Si hay un fosforo encendido
                propagada += [1]*cont
                
            else: # Si todos los fosforos estaban apagados
                propagada += fosforos
            
            propagada.append(-1)    
            cont = -1 # pongo -1 porque mas abajo incremetno 1 y quiero que quede en 0
            fosforos = [] #limpio la lista para el nuevo grupo de fosforos
        cont += 1
    
    #Al terminar la lista puede ocurrir que el ultimo grupo no se haya analizado (esto sucede cuando la lista NO termina en -1)
    #Para analizar y agregar este ultimo grupo chequeo el largo de la lista'fosforos'
    
    if len(fosforos)>0: #si len > 0 quiere decir que todavia queda un grupo de fosforos por agregar
        if 1 in fosforos: 
            propagada += [1]*cont
        else: 
            propagada += fosforos
            
    return propagada

lista = [ 0, 0, 0,-1, 1, 0, 0, 0,-1, 0, 1, 0, 0]
print(lista)
print(propagar(lista))

'''
[0, 0, 0, -1, 1, 0, 0, 0, -1, 0, 1, 0, 0]
[0, 0, 0, -1, 1, 1, 1, 1, -1, 1, 1, 1, 1]
'''

