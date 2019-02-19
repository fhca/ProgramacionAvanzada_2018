__author__ = 'fhca'


def verifica_si_esta_ordenada(lista):
    a = lista[0]
    for b in lista[1:]:
        if b < a:
            return False
        a = b
    return True


import time
import numpy as np


def t(n):
    suma = 0
    for _ in range(10):
        t0 = time.time()
        l = np.random.rand(n)
        verifica_si_esta_ordenada(l)
        suma += time.time() - t0
    return suma


x = np.arange(2, 10000, dtype=int)
y = np.array(list(map(t, x)))

import matplotlib.pyplot as plt

plt.figure()
plt.plot(x, y)
plt.show()
