__author__ = 'fhca'

import numpy as np

e = np.zeros(7, 13)

e[0, 1] = e[0, 3] = e[0, 4] = e[0, 5] = e[0, 8] = e[0, 11] = 1

""" 
e[5, -1]  <-- no es error, es la última columna
e[5, 13]  <-- error!, no hay columna 13
"""


def celda(e, i, j, f):
    """pone el valor 0 o 1 dependiendo de f,
    en la celda renglón i, columna j."""
    if j >= e.size[1]:  # num de columnas
        e[i, j] = f(e[i - 1, j - 1], e[i - 1, j], e[i - 1, 0])
    else:
        e[i, j] = f(e[i - 1, j - 1], e[i - 1, j], e[i - 1, j + 1])

def f(x, y, z, regla):
    pass

def funcion_regla(regla):
    regla/2
    return arreglo