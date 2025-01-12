class shape:
    def __init__(self, vertices: list, edges: list, angulos_internos: list):
        self.vertices = vertices
        self.edges = edges
        self.angulos_internos = angulos_internos
        if edges:
            self.es_poligono_regular = self._verificar_poligono_regular()
        else:
            self.es_poligono_regular = False

    def _verificar_poligono_regular(self):
        lados = [edge.largo for edge in self.edges]
        angulos = self.angulos_internos
        if lados and angulos: # Verificar que las listas no esten vacias
            return all(abs(lado - lados[0]) < 1e-9 for lado in lados) and all(abs(angulo - angulos[0]) < 1e-9 for angulo in angulos)
        return False

    def calcular_area(self):
        raise NotImplementedError("calcular_area debe ser implementado en las subclases")

    def calcular_perimetro(self):
        return sum(edge.largo for edge in self.edges) if self.edges else 0

    def calcular_angulos_internos(self):
        return self.angulos_internos