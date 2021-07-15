'''
total = 0
with open ("camion.csv", "rt") as f:
    headers = next(f)
    for line in f:
        row = line.split(',')
        total += float(row[1]) * float(row[2])
    print('Costo Total:', total)
'''

def costo_camion(archivo):
    total = 0
    with open (archivo, "rt") as f:
        headers = next(f)
        for line in f:
            row = line.split(',')
            total += float(row[1]) * float(row[2])
    return (total)

a = input('ingrese el nombre del archivo:')
costo = costo_camion(a)
print('Costo TOATAL:', costo)