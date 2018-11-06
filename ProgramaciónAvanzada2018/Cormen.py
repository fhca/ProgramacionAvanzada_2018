__author__ = 'fhca'

import numpy as np


class NuevaLista:
    """Para apegarse al libro Cormen, estas listas comienzan en 1 y terminan en índice n """

    def __init__(self, tam):
        self.chivito = np.random.randint(10, 1000, tam)

    def __repr__(self):
        return str(self.chivito)

    def __getitem__(self, item):
        return self.chivito[item - 1]

    def __setitem__(self, key, value):
        self.chivito[key - 1] = value
        return value

    def __len__(self):
        return self.chivito.size


def length(lista):
    return len(lista)


def ciclo(inicio=1, fin=1, paso=1):
    """ range para iterar listas que terminan en el valor 'fin'. """
    return range(inicio, fin + 1, paso)


INFINITO = np.inf
