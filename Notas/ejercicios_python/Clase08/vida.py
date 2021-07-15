#vida.py

#Author: Lucas Pangaro
#Mail: Pangaro.lucas@gmail.com
#Date: 12/05/21


#%%..:EJERCICIO 8.1:..
#%%
import datetime

print('Ingrese su fecha de nacimiento con el siguiente formato "dd/mm/AAAA" ')
nacimiento = input()
nacimiento = datetime.datetime.strptime(nacimiento, '%d/%m/%Y')

actual = datetime.datetime.now()

diferencia = actual - nacimiento


print('Usted vivio', diferencia.total_seconds(),'segundos')


