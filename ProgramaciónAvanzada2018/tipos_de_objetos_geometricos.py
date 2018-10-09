__author__ = 'fhca'

import objetos_geometricos as og


class Triangulo(og.ObjetoGeometrico):
    def __init__(self, a=0, b=0, c=0):
        super().__init__(como_se_llama="Triángulo")
        self.a = a
        self.b = b
        self.c = c

    def calcula_base_y_altura(self):
        self.base = self.c
        self.altura = self.b


    def area(self):
        self.calcula_base_y_altura()
        return self.base * self.altura / 2

    def perimetro(self):
        return


class Cuadrado(og.ObjetoGeometrico):
    def __init__(self):
        super().__init__("Cuadrado")


class Rectangulo(Cuadrado):
    def __init__(self):
        super().__init__()


t = Triangulo()
r = Rectangulo()

t.dame_info("t")
r.dame_info("r")
print(isinstance(r, Rectangulo))
