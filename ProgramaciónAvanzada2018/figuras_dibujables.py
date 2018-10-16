__author__ = 'fhca'

from objetos_dibujables import Dibujable
from tipos_de_objetos_geometricos import *


def distancia(a, b):
    xa, ya = a
    xb, yb = b
    return np.sqrt((xb - xa) ** 2 + (yb - ya) ** 2)


class TrianguloDibujable(Triangulo, Dibujable):
    def __init__(self):
        Dibujable.__init__(self)
        radio = np.random.random() * 30 + 10
        alfa = np.random.rand(3) * 2 * np.pi
        self.v0 = np.array((radio * np.cos(alfa[0]), radio * np.sin(alfa[0])))
        self.v1 = np.array((radio * np.cos(alfa[1]), radio * np.sin(alfa[1])))
        self.v2 = np.array((radio * np.cos(alfa[2]), radio * np.sin(alfa[2])))
        Triangulo.__init__(self,
                           distancia(self.v0, self.v1),
                           distancia(self.v1, self.v2),
                           distancia(self.v2, self.v0))

    def pinta(self):
        a0 = self.v0 + self.posicion
        a1 = self.v1 + self.posicion
        a2 = self.v2 + self.posicion
        Dibujable.lienzo.create_polygon(*a0, *a1, *a2, fill="white", outline="blue")


class CuadradoDibujable(Cuadrado, Dibujable):
    pass


class RectanguloDibujable(Rectangulo, Dibujable):
    pass


t = []
for _ in range(50):
    t.append(TrianguloDibujable())
    t[-1].pinta()

import tkinter as tk

tk.mainloop()
