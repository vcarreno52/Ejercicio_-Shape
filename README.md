# EJERCICIO SHAPE 
##Reto 5 
<P>
Cree un paquete con todo el código del ejercicio Shape, este código debe se relaizarse dos maneras: 
- Primer forma:
Un módulo único dentro del paquete Shape
- Segunda forma: 
Los módulos individuales que importan Shape heredan de él. 

</P>
### Instrucciones ejercicio shape 
<p>
- Create a superclass called Shape(), which is the base of the classes Reactangle() and Square(), define the methods compute_area and compute_perimeter in Shape() and then using polymorphism redefine the methods proprly in Rectangle and in Square.
- Using the classes Point() and Line() define a new super-class Shape() 
</p>

Primera forma 
-------------------------------
![](https://github.com/vcarreno52/Ejercicio_-Shape/blob/main/Carpeta%20Altenativa%201.png?raw=true)

#__init__


    
        from .Shapes import Punto, Linea, Triangulo, TrianguloEquilatero, TrianguloIsosceles, TrianguloRectangulo, TrianguloEscaleno, Rectangulo, Cuadrado


#Shapes


    
        import math

        class Punto:
            def __init__(self, x: float, y: float):
                self.x = x
                self.y = y
            def calcular_distancia(self, otro_punto):
              return math.sqrt((self.x - otro_punto.x)**2 + (self.y - otro_punto.y)**2)


        class Linea:
            def __init__(self, punto_inicial: Punto, punto_final: Punto):
                self.punto_inicial = punto_inicial
                self.punto_final = punto_final
                self.largo = self.calcular_largo()
        
            def calcular_largo(self):
                return self.punto_inicial.calcular_distancia(self.punto_final)
        
        
        class Figura:
            def __init__(self, vertices: list[Punto], edges: list[Linea], angulos_internos: list[float]):
                self.vertices = vertices
                self.edges = edges
                self.angulos_internos = angulos_internos
                self.es_poligono_regular = self._verificar_poligono_regular()
        
            def _verificar_poligono_regular(self):
                lados = [edge.largo for edge in self.edges]
                angulos = self.angulos_internos
                return all(lado == lados[0] for lado in lados) and all(angulo == angulos[0] for angulo in angulos)
        
            def calcular_area(self):
                pass
        
            def calcular_perimetro(self):
                return sum(edge.largo for edge in self.edges)
        
            def calcular_angulos_internos(self):
                return self.angulos_internos
        
        
        class Triangulo(Figura):
            def calcular_area(self):
                a, b, c = [edge.largo for edge in self.edges]
                s = (a + b + c) / 2
                return math.sqrt(s * (s - a) * (s - b) * (s - c))
        
        
        class TrianguloIsosceles(Triangulo):
            def calcular_area(self):
                a, b, c = [edge.largo for edge in self.edges]
                if a == b or b == c or a == c:
                    s = (a + b + c) / 2
                    return math.sqrt(s * (s - a) * (s - b) * (s - c))
                return ("No es isósceles")
        
        
        class TrianguloEscaleno(Triangulo):
            def calcular_area(self):
                a, b, c = [edge.largo for edge in self.edges]
                if a != b and b != c and a != c:
                    s = (a + b + c) / 2
                    return math.sqrt(s * (s - a) * (s - b) * (s - c))
        
        class TrianguloRectangulo(Triangulo):
            def calcular_area(self):
                a, b, c = sorted([edge.largo for edge in self.edges])
                return (a * b) / 2
        
        
        class TrianguloEquilatero(Triangulo):
            def calcular_area(self):
                a = self.edges[0].largo
                return (math.sqrt(3) / 4) * (a ** 2)
        
        
        class Rectangulo(Figura):
            def calcular_area(self):
                a, b = [self.edges[0].largo, self.edges[1].largo]
                return a * b
        
        
        class Cuadrado(Rectangulo):
            def calcular_area(self):
                lado = self.edges[0].largo
                return lado ** 2
        
            def calcular_perimetro(self):
                lado = self.edges[0].largo
                return 4 * ladohapes import Punto, Linea, Triangulo, TrianguloEquilatero, TrianguloIsosceles, TrianguloRectangulo,                        TrianguloEscaleno, Rectangulo, Cuadrado

Segunda forma 
-------------------------------
![]()

            
    
