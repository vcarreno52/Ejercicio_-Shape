from .punto import Punto    

class Linea:
    def __init__(self, punto_inicial: Punto, punto_final: Punto):
        self.punto_inicial = punto_inicial
        self.punto_final = punto_final
        self.largo = self.calcular_largo()

    def calcular_largo(self):
        return self.punto_inicial.calcular_distancia(self.punto_final)