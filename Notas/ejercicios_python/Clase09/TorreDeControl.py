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
       '''Devuelve el próximo elemento sin desencolar
       Requiere que la cola no sea vacía'''
       if len(self.items_con_prioridad):
           res = self.items_con_prioridad[0]
       else:
           res = self.items[0]
       return res
