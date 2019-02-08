__author__ = 'fhca'

import numpy as np
import tkinter as tk


class Dibujable:
    try:
        lienzo
    except NameError:
        lienzo_dim = np.array((550, 550))
        lienzo = tk.Canvas(width=lienzo_dim[0], height=lienzo_dim[1], bg='white')
        lienzo.pack(expand=tk.YES, fill=tk.BOTH)

    def __init__(self):
        self.posicion = np.random.rand(2) * Dibujable.lienzo_dim  # posición son dos coord. al azar

    def pinta(self):
        pass

    def avanza(self, dx, dy):
        "'incrementa' la posición en (dx, dy)"
        self.posicion = self.posicion + np.array((dx, dy))


    def mueve_a_xy(self, x, y):
        """Mueve el objeto a la posición (x,y)."""
        self.posicion = np.array((x, y))
