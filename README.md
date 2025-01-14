# EJERCICIO SHAPE 
## Reto 5 
<P>
Cree un paquete con todo el código del ejercicio Shape, este código debe se relaizarse dos maneras: 
- Primer forma:
Un módulo único dentro del paquete Shape
- Segunda forma: 
Los módulos individuales que importan Shape heredan de él. 

</P>
## Instrucciones ejercicio shape 
<p>
- Create a superclass called Shape(), which is the base of the classes Reactangle() and Square(), define the methods compute_area and compute_perimeter in Shape() and then using polymorphism redefine the methods proprly in Rectangle and in Square.
- Using the classes Point() and Line() define a new super-class Shape() 
</p>

Primera forma 
-------------------------------
![](https://github.com/vcarreno52/Ejercicio_-Shape/blob/main/Carpeta%20Altenativa%201.png?raw=true)

#__init__
#main


            
                from Shapes import *

                #pueba sugerida por copilot 
                A= Punto(1, 1)
                B= Punto(1, 2)  
                M= (A.CalcularDistancia(B)) # 1.0
                print (M)
                
                A = Punto(1, 1)     
                B = Punto(2, 2)
                
                M= (A.CalcularDistancia(B)) # 1.4142135623730951
                print(M)
                
                l= Linea(A,B)
                print(l.largo) 
                
                p= [Punto(0,0), Punto(0,1), Punto(1,1), Punto(1,0)]
                l = [Linea(p[0], p[1]), Linea(p[1], p[2]), Linea(p[2], p[3]), Linea(p[3], p[0])]
                a = [90, 90, 90, 90]
                
                s = Shape(p, l, a)
                print(s.calcular_perimetro())
                print(s.es_poligono_regular)
                print(s.calcular_angulos_internos())



#Shapes


                                                class Punto:
                                                    def __init__(self, x:float, y:float):
                                                        self.x = x
                                                        self.y = y
                                                    
                                                    def CalcularDistancia(self, punto):
                                                        return ((self.x - punto.x)**2 + (self.y - punto.y)**2)**0.5
                                                
                                                
                                                class Linea:
                                                    def __init__(self, punto_inicial:Punto, punto_final:Punto):
                                                        self.punto_inicial = punto_inicial	
                                                        self.punto_final = punto_final
                                                        self.largo = self.Calcular_largo() 
                                                    def Calcular_largo(self):
                                                        return self.punto_inicial.CalcularDistancia(self.punto_final)
                                                    
                                                
                                                class Shape:
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
                                                    
                                                
                                                class Triangulo(Shape):
                                                    def calcular_area(self):
                                                        a, b, c = [edge.largo for edge in self.edges]
                                                        s = (a + b + c) / 2
                                                        return ((s * (s - a) * (s - b) * (s - c)))**0.5
                                                
                                                
                                                class TrianguloIsosceles(Triangulo):
                                                    def calcular_area(self):
                                                        a, b, c = [edge.largo for edge in self.edges]
                                                        if a == b or b == c or a == c:
                                                            s = (a + b + c) / 2
                                                            return ((s * (s - a) * (s - b) * (s - c)))**0.5
                                                        return ("No es isósceles")
                                                
                                                
                                                class TrianguloEscaleno(Triangulo):
                                                    def calcular_area(self):
                                                        a, b, c = [edge.largo for edge in self.edges]
                                                        if a != b and b != c and a != c:
                                                            s = (a + b + c) / 2
                                                            return ((s * (s - a) * (s - b) * (s - c)))**0.5
                                                
                                                class TrianguloRectangulo(Triangulo):
                                                    def calcular_area(self):
                                                        a, b, c = sorted([edge.largo for edge in self.edges])
                                                        return (a * b) / 2
                                                    
                                                class TrianguloEquilatero(Triangulo):
                                                    def calcular_area(self):
                                                        a = self.edges[0].largo
                                                        return ((3)**1/2 / 4) * (a ** 2)
                                                
                                                
                                                class Rectangulo(Shape):
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

                                                        
Segunda forma 
-------------------------------
![](https://github.com/vcarreno52/Ejercicio_-Shape/blob/main/Carpeta%20Alternativa2.png?raw=true)



Caperta shape 
#__init__



                                                
#Rectángulo 



                                                from shapes import shape    
                                                
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
                                                        
#Shape


                                                from punto import Punto 
                                                from Linea import Linea 
                                                
                                                class shape:
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
                                                                        

#Triangulo


                                                from shapes import shape
                                                
                                                class Triangulo(shape):
                                                    def calcular_area(self):
                                                        a, b, c = [edge.largo for edge in self.edges]
                                                        s = (a + b + c) / 2
                                                        return ((s * (s - a) * (s - b) * (s - c)))**0.5
                                                
                                                
                                                class TrianguloIsosceles(Triangulo):
                                                    def calcular_area(self):
                                                        a, b, c = [edge.largo for edge in self.edges]
                                                        if a == b or b == c or a == c:
                                                            s = (a + b + c) / 2
                                                            return ((s * (s - a) * (s - b) * (s - c)))**0.5
                                                        return ("No es isósceles")
                                                
                                                
                                                class TrianguloEscaleno(Triangulo):
                                                    def calcular_area(self):
                                                        a, b, c = [edge.largo for edge in self.edges]
                                                        if a != b and b != c and a != c:
                                                            s = (a + b + c) / 2
                                                            return ((s * (s - a) * (s - b) * (s - c)))**0.5
                                                
                                                class TrianguloRectangulo(Triangulo):
                                                    def calcular_area(self):
                                                        a, b, c = sorted([edge.largo for edge in self.edges])
                                                        return (a * b) / 2
                                                    
                                                class TrianguloEquilatero(Triangulo):
                                                    def calcular_area(self):
                                                        a = self.edges[0].largo
                                                        return ((3)**1/2 / 4) * (a ** 2)

        
#__init__


                                                
-----------------------
#Punto 


                                                class Punto:
                                                    def __init__(self, x:float, y:float):
                                                        self.x = x
                                                        self.y = y
                                                    
                                                    def CalcularDistancia(self, punto):
                                                        return ((self.x - punto.x)**2 + (self.y - punto.y)**2)**0.5
                            
#Linea


                                                
                                                from punto import Punto
                                                
                                                class Linea:
                                                    def __init__(self, punto_inicial:Punto, punto_final:Punto):
                                                        self.punto_inicial = punto_inicial	
                                                        self.punto_final = punto_final
                                                        self.largo = self.Calcular_largo() 
                                                    def Calcular_largo(self):
                                                        return self.punto_inicial.CalcularDistancia(self.punto_final)
                                                    

# main 


                                                from punto import Punto
                                                from Linea import Linea
                                                from Shapes.shapes import shape
                                                #from Shapes.Rectángulo import Rectangulo, Cuadrado  
                                                #from Shapes.triangulo import *
                                                #No son necesarios para esta prueba
                                                
                                                
                                                
                                                A= Punto(1, 1)
                                                B= Punto(1, 2)  
                                                M= (A.CalcularDistancia(B)) # 1.0
                                                print (M)
                                                
                                                A = Punto(1, 1)     
                                                B = Punto(2, 2)
                                                
                                                M= (A.CalcularDistancia(B)) # 1.4142135623730951
                                                print(M)
                                                
                                                l= Linea(A,B)
                                                print(l.largo) # 1.4142135623730951
                                                
                                                p= [Punto(0,0), Punto(0,1), Punto(1,1), Punto(1,0)]
                                                l = [Linea(p[0], p[1]), Linea(p[1], p[2]), Linea(p[2], p[3]), Linea(p[3], p[0])]
                                                a = [90, 90, 90, 90]
                                                
                                                s = shape(p, l, a)
                                                print(s.calcular_perimetro())
                                                print(s.es_poligono_regular)
                                                print(s.calcular_angulos_internos())


                    


            
    
