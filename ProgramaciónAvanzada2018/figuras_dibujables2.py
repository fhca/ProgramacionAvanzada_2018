__author__ = 'fhca'

from objetos_dibujables2 import Dibujable
from tipos_de_objetos_geometricos2 import *


def distancia(a, b):
    xa, ya = a
    xb, yb = b
    return np.sqrt((xb - xa) ** 2 + (yb - ya) ** 2)


class TrianguloDibujable(Triangulo, Dibujable):
    """centro: punto relativo al cual se pintan los otros vértices de este polígono
    posicion: desplazamiento del poligono
    """

    def __init__(self):
        Dibujable.__init__(self)
        radio = np.random.random() * 30 + 10
        alfa = np.random.rand(3) * 2 * np.pi
        self.v0 = np.array((radio * np.cos(alfa[0]), radio * np.sin(alfa[0]))) - self.centro
        self.v1 = np.array((radio * np.cos(alfa[1]), radio * np.sin(alfa[1]))) - self.centro
        self.v2 = np.array((radio * np.cos(alfa[2]), radio * np.sin(alfa[2]))) - self.centro
        self.orientacion = alfa[0]
        Triangulo.__init__(self,
                           distancia(self.v0, self.v1),
                           distancia(self.v1, self.v2),
                           distancia(self.v2, self.v0))
        self.pinta()

    def pinta(self):
        a0 = self.v0 + self.centro + self.posicion
        a1 = self.v1 + self.centro + self.posicion
        a2 = self.v2 + self.centro + self.posicion
        # self.id es el consecutivo identificador de este objeto
        self.id = Dibujable.lienzo.create_polygon(*a0, *a1, *a2, fill="white", outline="blue")


class CuadradoDibujable(Cuadrado, Dibujable):
    pass


class RectanguloDibujable(Rectangulo, Dibujable):
    pass


def crt(n):
    return [TrianguloDibujable() for _ in range(n)]  # _ = variable Voldemort (segun Paty)


def avanza(coleccion):
    for t in coleccion:
        t.avanza()


coleccion = crt(20)


def animacion():
    #while True:  # no se debe hacer un ciclo infinito para animar dibujos con tkinter
    avanza(coleccion)
    Dibujable.lienzo.master.after(12, animacion)


# Dibujable.lienzo.master.after(0, animacion)

animacion()

Dibujable.lienzo.mainloop()
