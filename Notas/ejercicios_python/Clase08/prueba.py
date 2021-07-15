#%%
def main(parametros):
    import os
  
    if (len (parametros) == 2):
        path = sys.argv[1]
    else:
        path = input('ingrese el path: ')

    for root, dirs, files in os.walk(path):
        for name in files:
            if '.png' in name:
                print(f'\x1b[1;33m {os.path.join(root, name)}')
        for name in dirs:
            print(f'\x1b[1;35m {os.path.join(root, name)}')
  

if __name__ == '__main__':
    import sys
    import os
    main(sys.argv)

    print('hola')
