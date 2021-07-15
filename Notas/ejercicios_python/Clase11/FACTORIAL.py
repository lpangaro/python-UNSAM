def sumar(lista):
   """Devuelve la suma de los elementos en la lista."""
   res = 0
   if len(lista) != 0:
       res = lista[0] + sumar(lista[1:])
       
   print(res)
   return res


lista = [0,1,2,3,4,5,6,7,8,9]
print(sumar(lista))