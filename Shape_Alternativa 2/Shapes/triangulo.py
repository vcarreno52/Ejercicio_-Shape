import math
from geometria.figuras.figura import Figura

class Triangulo(Figura):
    def calcular_area(self):
        a, b, c = [edge.largo for edge in self.edges]
        s = (a + b + c) / 2
        return math.sqrt(s * (s - a) * (s - b) * (s - c)) if a > 0 and b > 0 and c > 0 and s > 0 and (s-a) > 0 and (s-b) > 0 and (s-c) > 0 else 0

class TrianguloIsosceles(Triangulo):
    pass #No es necesario redefinir calcular_area

class TrianguloEscaleno(Triangulo):
    pass #No es necesario redefinir calcular_area

class TrianguloRectangulo(Triangulo):
    def calcular_area(self):
        lados = sorted([edge.largo for edge in self.edges])
        return (lados[0] * lados[1]) / 2 if lados[0] > 0 and lados[1] > 0 else 0

class TrianguloEquilatero(Triangulo):
    def calcular_area(self):
        a = self.edges[0].largo
        return (math.sqrt(3) / 4) * (a ** 2) if a > 0 else 0
    