"""Localiza el menor valor de una lista de números"""

def minimo(a):
    min = a[0]
    for elemento in a[1:]:
        if elemento < min:
            min = elemento
    return min

def maximo(a):
    max = a[0]
    for elemento in a[1:]:
        if elemento > max:
            max = elemento
    return max

a = [52,54235,4325,4325,45,23,5435,245,423,5432,543,34,75]
from time import time
t0 = time()
print(minimo(a))
t1 = time()
print(maximo(a))
t2 = time()

print("mínimo:", t1-t0, "máximo:", t2-t1)
