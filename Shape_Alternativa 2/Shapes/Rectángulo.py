from shape import shape

class Rectangulo(shape):
    def calcular_area(self):
        a, b = [self.edges[0].largo, self.edges[1].largo]
        return a * b


class Cuadrado(Rectangulo):
    def calcular_area(self):
        lado = self.edges[0].largo
        return lado ** 2

    def calcular_perimetro(self):
        lado = self.edges[0].largo
        return 4 * lado
