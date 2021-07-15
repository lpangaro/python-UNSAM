#listar_imgs.py

#Author: Lucas Pangaro
#Mail: Pangaro.lucas@gmail.com
#Date: 12/05/21


#%%..:EJERCICIO 8.5:..
#%%
def main(parametros):

    if (len(parametros) == 2):
        path = sys.argv[1]
    else:
        path = input('ingrese el path: ')

    for root, dirs, files in os.walk(path):
        for name in files:
            if '.png' in name:
                print(f'\x1b[1;33m {os.path.join(root, name)} \x1b[1;0m')
        for name in dirs:
            print(f'\x1b[1;35m {os.path.join(root, name)} x1b[1;0m')


#%%
if __name__ == '__main__':
    import sys
    import os
    main(sys.argv)
