import math 
class Punto:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def calcular_distancia(self, otro_punto):
        return math.sqrt((self.x - otro_punto.x)**2 + (self.y - otro_punto.y)**2)