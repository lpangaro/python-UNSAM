#%%
import os

print ( os.getcwd() ) #Muestra el directorio actual
os.mkdir( 'mi_directorio') #creo un directorio
os.chdir('mi_directorio') #me muevo a ese directorio, seria como el cd
os. rmdir('mi_directorio') ## Borro el directorio

os.listdir('./data') # muestra una lista de archivos que tiene el directorio
os.rename('mi_directorio', 'mi_dir')
