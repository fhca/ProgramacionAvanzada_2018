__author__ = 'fhca'
import numpy as np
from objetos_geometricos import ObjetoGeometrico


class Punto(ObjetoGeometrico):
    def __init__(self, x=0, y=0):
        super().__init__(como_se_llama="Punto")
        self.x = x
        self.y = y


class Triangulo(ObjetoGeometrico):
    def __init__(self, a=0, b=0, c=0):
        """a,b,c son longitudes de lados"""
        super().__init__(como_se_llama="Triángulo")
        self.a = a
        self.b = b
        self.c = c
        if not ((a < b + c) and (b < a + c) and (c < a + b)):
            print("Error, triángulo inválido.")

    def area(self):
        p = self.perimetro() / 2
        return np.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))

    def perimetro(self):
        return self.a + self.b + self.c


class Cuadrado(ObjetoGeometrico):
    def __init__(self, a=0):
        super().__init__("Cuadrado")
        self.a = a

    def area(self):
        return self.a ** 2

    def perimetro(self):
        return 4 * self.a


class Rectangulo(Cuadrado):
    def __init__(self, a=0, b=0):
        super().__init__("Rectángulo")
        self.a = a
        self.b = b

    def area(self):
        return self.a * self.b

    def perimetro(self):
        return self.a * 2 + self.b * 2


if __name__ == '__main__':
    t = Triangulo(9, 4, 6)
    r = Rectangulo(4, 3)
    p = Punto()
    c = Cuadrado(2, 2)

    t.dame_info("t")
    r.dame_info("r")
    p.dame_info("p")
    c.dame_info("c")
