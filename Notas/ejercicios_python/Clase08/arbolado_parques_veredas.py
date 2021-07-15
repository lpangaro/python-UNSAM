#arbolado_parques_veredas.py

#Author: Lucas Pangaro
#Mail: Pangaro.lucas@gmail.com
#Date: 12/05/21


#%%..:EJERCICIO 8.9:..

import pandas as pd


df_parques = pd.read_csv('../Data/arbolado-en-espacios-verdes.csv')
df_veredas = pd.read_csv('../Data/arbolado-publico-lineal-2017-2018.csv')

x = df_parques['nombre_com'] == 'Jacarandá'

#Selecciona las columnas que voy a necesitar
cols_parques = ['diametro', 'altura_tot' ]
cols_veredas = ['diametro_altura_pecho', 'altura_arbol']

#COPIO los datos de cols a nuevos DataFrame
df_tipas_parques = df_parques[df_parques['nombre_cie'] == 'Tipuana Tipu'][cols_parques].copy()
df_tipas_veredas = df_veredas[df_veredas['nombre_cientifico'] == 'Tipuana tipu'][cols_veredas].copy()

#cambio el nombre de las columnas
df_tipas_parques = df_tipas_parques.rename(columns={'altura_tot' : 'altura'})
df_tipas_veredas = df_tipas_veredas.rename(columns={'diametro_altura_pecho' : 'diametro', 'altura_arbol' : 'altura'})

#Agrego una columna con Ambiente
df_tipas_parques = df_tipas_parques.assign(ambiente = 'parque')
df_tipas_veredas = df_tipas_veredas.assign(ambiente = 'vereda')

#Uno ambos Data Frame
df_tipas = pd.concat([df_tipas_veredas, df_tipas_parques])

#graficos
df_tipas.boxplot('diametro',by = 'ambiente')
df_tipas.boxplot('altura',by = 'ambiente')