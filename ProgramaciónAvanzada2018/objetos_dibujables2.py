__author__ = 'fhca'

import numpy as np
import tkinter as tk


class Dibujable:
    if not "lienzo" in globals():
        lienzo_dim = np.array((550, 550))
        lienzo = tk.Canvas(width=lienzo_dim[0], height=lienzo_dim[1], bg='black')
        lienzo.pack(expand=tk.YES, fill=tk.BOTH)
        paso = .5

    def __init__(self):
        self.centro = np.random.rand(2) * Dibujable.lienzo_dim  # posición son dos coord. al azar
        self.posicion = self.centro
        self.orientacion = 0
        self.id = 0

    def pinta(self):
        pass

    def mueve_a_xy(self, x, y):
        """Mueve el objeto a la posición (x,y)."""
        self.posicion = np.array((x, y))

    def mueve_centro_a_xy(self, x, y):
        self.centro = np.array((x, y))

    def avanza(self, n=1):
        """:type n:int  = número de pasos"""
        self.posicion += np.array(np.cos(self.orientacion), np.sin(self.orientacion)) * Dibujable.paso * n
        Dibujable.lienzo.delete(self.id)  # borra dibujo anterior
        self.pinta()  # dibujo en la nueva posición
        # versión en tkinter...
        # Dibujable.lienzo.move(self.id, Dibujable.paso * n * np.cos(self.orientacion),
        #                      Dibujable.paso * n * np.sin(self.orientacion))
