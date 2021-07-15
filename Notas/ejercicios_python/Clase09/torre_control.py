#torre_control.py

#Author: Lucas Pangaro
#Mail: Pangaro.lucas@gmail.com

# ..:EJERCICIO 9.12:..
class TorreDeControl:
    def __init__(self):
        '''Crea una cola vacia.'''
        self.items = []
        self.items_con_prioridad = []
        
    def nuevo_arribo(self, x):
        '''Encola el elemento x.'''
        self.items_con_prioridad.append(x)
        
    def nueva_partida(self, x):
      '''Encola el elemento x.'''
      self.items.append(x)  
      
    def ver_estado(self):
        res = 'Vuelos esperando para aterrizar: '
        res += ', '.join(self.items_con_prioridad)
        res +='\n'
        res += 'Vuelos esperando para despegar: '
        res += ','.join(self.items)
        
        print(res)
        
    def asignar_pista(self):
        '''Elimina el primer elemento de la cola.
        Si la cola esta vacia, levanta ValueError.'''
        if self.esta_vacia():
            raise ValueError('No hay vuelos en espera')
        
        else: 
            if len(self.items_con_prioridad):
                res = self.items_con_prioridad.pop(0)
                print(f'El vuelo {res} aterrizo con exito')
            else:
                res = self.items.pop(0)
                print(f'El vuelo {res} despego con exito')
    
    def largo_cola(self):
        '''Devuelve el largo de la cola.'''
        return len(self.items) + len(self.items_con_prioridad)

    def esta_vacia(self):
        '''Devuelve
        True si la cola esta vacia,
        False si no.'''
        return self.largo_cola() == 0