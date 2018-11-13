__author__ = 'fhca'

"""Algoritmos para ordenar una lista (de números). """

from Cormen import *

"""Ordena, método 1"""


def ordena_insercion(A):
    for j in ciclo(2, longitud(lista)):
        key = A[j]
        i = j - 1
        while i > 0 and A[i] > key:
            A[i + 1] = A[i]
            i = i - 1
        A[i + 1] = key


"""NuevaLista genera una lista de enteros al azar (entre 10 y 1000)"""


# lista = NuevaLista(100)  # lista de 10 enteros al azar
# print(lista)
# ordena_insercion(lista)
# print(lista)


def mezcla(A, p, q, r):
    n1 = q - p + 1
    n2 = r - q
    # creando arreglos L[1..n1+1] y R[1..n2+1]
    L = NuevaLista(n1 + 1)
    R = NuevaLista(n2 + 1)
    for i in ciclo(1, n1):
        L[i] = A[p + i - 1]
    for j in ciclo(1, n2):
        R[j] = A[q + j]
    L[n1 + 1] = INFINITO
    R[n2 + 1] = INFINITO
    i = 1
    j = 1
    for k in ciclo(p, r):
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1


def ordena_mezclas(A, p, r):
    if p < r:
        q = piso((p + r) / 2)
        ordena_mezclas(A, p, q)
        ordena_mezclas(A, q + 1, r)
        mezcla(A, p, q, r)


lista = NuevaLista(100)
print(lista)
ordena_mezclas(lista, 1, 100)
print(lista)
