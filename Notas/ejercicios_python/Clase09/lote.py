#lote.py

#Author: Lucas Pangaro
#Mail: Pangaro.lucas@gmail.com

# ..:EJERCICIO 9.9:..
class Lote():
    def __init__(self, nombre, cajones, precio):
        self.nombre = nombre
        self.cajones = cajones
        self.precio = precio
        
    def costo(self):
        costo = self.cajones * self.precio
        return costo
        
    def vender(self, cant):
        self.cajones -= cant        
        

    def __repr__ (self):
        return f'\x1b[1;35mLote (\x1b[0m {self.nombre}, {self.cajones}, {self.precio} \x1b[1;35m)'
