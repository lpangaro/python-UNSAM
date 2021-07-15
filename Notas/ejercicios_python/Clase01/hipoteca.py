 # hipoteca.py

#Author: Lucas Pangaro
#Mail: Pangaro.lucas@gmail.com
#Date: 10/3/21

# ..:ENUNCIADO 1.7:..
#David solicitó un crédito a 30 años para comprar una vivienda, con una tasa fija nominal anual del 5%. Pidió $500000 al banco y acordó un pago mensual fijo de $2684,11
''''
saldo = 500000.0
tasa = 0.05
pago_mensual = 2684.11
total_pagado = 0.0

while saldo > 0:
    saldo = saldo * (1+tasa/12) - pago_mensual
    total_pagado = total_pagado + pago_mensual

print('Total pagado', round(total_pagado, 2))
'''

# ..:ENUNCIADO 1.8:..
# Supongamos que David adelanta pagos extra de $1000/mes durante los primeros 12 meses de la hipoteca.
# Modificá el programa para incorporar estos pagos extra y que imprima el monto total pagado junto con la cantidad de meses requeridos.
'''
saldo = 500000.0
tasa = 0.05
pago_mensual = 2684.11
total_pagado = 0.0

adelanto = 1000.0
mes = 0

while saldo > 0:

    if mes < 12:
        saldo = saldo * (1+tasa/12) - pago_mensual - adelanto
        total_pagado = total_pagado + pago_mensual + adelanto

    else:
        saldo = saldo * (1+tasa/12) - pago_mensual
        total_pagado = total_pagado + pago_mensual
    mes = mes + 1
print('Total pagado', round(total_pagado, 2))
print('Meses: ', mes)
'''


# ..:ENUNCIADO 1.9:..
#¿Cuánto pagaría David si agrega $1000 por mes durante cuatro años, comenzando en el sexto año de la hipoteca (es decir, luego de 5 años)?
'''
saldo = 500000.0
tasa = 0.05
pago_mensual = 2684.11
total_pagado = 0.0

mes = 0
adelanto = 1000.0

pago_extra_mes_comienzo = 61
pago_extra_mes_fin = 108
pago_extra = 1000

while saldo > 0:

    if mes < 12:
        saldo = saldo * (1+tasa/12) - pago_mensual - adelanto
        total_pagado = total_pagado + pago_mensual + adelanto

    elif mes > pago_extra_mes_comienzo and mes < pago_extra_mes_fin:
        saldo = saldo * (1+tasa/12) - pago_mensual - pago_extra
        total_pagado = total_pagado + pago_mensual + pago_extra

    else:
        saldo = saldo * (1+tasa/12) - pago_mensual
        total_pagado = total_pagado + pago_mensual
    mes = mes + 1
print('Total pagado', round(total_pagado, 2))
print('Meses: ', mes)
'''

# ..:ENUNCIADO 1.10:..
# Modicá tu programa para que imprima una tabla mostrando el mes, el total pagado hasta el momento y el saldo restante. 
'''
aldo = 500000.0
tasa = 0.05
pago_mensual = 2684.11
total_pagado = 0.0

mes = 1
adelanto = 0.0

pago_extra_mes_comienzo = 61
pago_extra_mes_fin = 108
pago_extra = 1000.0

while saldo > 0:

    if mes < 12:
        saldo = saldo * (1+tasa/12) - pago_mensual - adelanto
        total_pagado = total_pagado + pago_mensual + adelanto

    elif mes >= pago_extra_mes_comienzo and mes <= pago_extra_mes_fin:
        saldo = saldo * (1+tasa/12) - pago_mensual - pago_extra
        total_pagado = total_pagado + pago_mensual + pago_extra

    else:
        saldo = saldo * (1+tasa/12) - pago_mensual
        total_pagado = total_pagado + pago_mensual
    mes = mes + 1

    print (mes-1," | ", round(total_pagado, 2)," | ",round(saldo, 2))

print('Total pagado', round(total_pagado, 2))
print('Meses: ', mes-1)s
'''
# ..:ENUNCIADO 1.11:..
# Ya que estamos, corregí el código anterior de forma que el pago del último mes se ajuste a lo adeudado.
saldo = 500000.0
tasa = 0.05
pago_mensual = 2684.11
total_pagado = 0.0

mes = 1
adelanto = 0.0

pago_extra_mes_comienzo = 61
pago_extra_mes_fin = 108
pago_extra = 1000.0

ultimo_pago = 0.0

while (saldo * (1+tasa/12) - pago_mensual) > 0:

    if mes < 12:
        saldo = saldo * (1+tasa/12) - pago_mensual - adelanto
        total_pagado = total_pagado + pago_mensual + adelanto

    elif mes >= pago_extra_mes_comienzo and mes <= pago_extra_mes_fin:
        saldo = saldo * (1+tasa/12) - pago_mensual - pago_extra
        total_pagado = total_pagado + pago_mensual + pago_extra

    else:
        saldo = saldo * (1+tasa/12) - pago_mensual
        total_pagado = total_pagado + pago_mensual
    mes = mes + 1

    print (mes-1," | ", "{0:.2f}".format(total_pagado)," | ","{0:.2f}".format(saldo)) #imprimo mes -1 porque empiezo en mes 1 en vez de 0


ultimo_pago = saldo * (1+tasa/12)

saldo = saldo * (1+tasa/12) - ultimo_pago
total_pagado = total_pagado + ultimo_pago
print (mes," | ", "{0:.2f}".format(total_pagado)," | ","{0:.2f}".format(saldo)) #imprimo mes sin el -1 porque fuera del while no sume mes=mes+1

print('Total pagado', round(total_pagado, 2))
print('Meses: ', mes)

'''
Output:
.
.
.
306  |  869337.66  |  8784.87
307  |  872021.77  |  6137.36
308  |  874705.88  |  3478.83
309  |  877389.99  |  809.21
310  |  878202.57  |  0.00

Total pagado 878202.57
Meses:  310
'''