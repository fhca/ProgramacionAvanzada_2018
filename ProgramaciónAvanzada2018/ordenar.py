__author__ = 'fhca'

"""Algoritmos para ordenar una lista (de números). """

from Cormen import *

"""NuevaLista genera una lista de enteros al azar (entre 10 y 1000)"""
lista = NuevaLista(100)  # lista de 10 enteros al azar

"""Ordena, método 1"""


def ordena_insercion(A):
    for j in ciclo(2, length(lista)):
        key = A[j]
        i = j - 1
        while i > 0 and A[i] > key:
            A[i + 1] = A[i]
            i = i - 1
        A[i + 1] = key


print(lista)
ordena_insercion(lista)
print(lista)
