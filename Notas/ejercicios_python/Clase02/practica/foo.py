'''
numero_valido=False
while not numero_valido:
    try:
        a = input('Ingresá un número entero: ')
        n = int(a)
        numero_valido = True
    except ValueError:   # con ctrl C sale del programa dando error
        print('No es válido. Intentá de nuevo.')
print(f'Ingresaste {n}.')
'''
numero_valido=False
while not numero_valido:
    try:
        a = input('Ingresá un número entero: ')
        n = int(a)
        numero_valido = True
    except:   #toma ctrl C como otra letra y no sale del programa
        print('No es válido. Intentá de nuevo.')
print(f'Ingresaste {n}.')