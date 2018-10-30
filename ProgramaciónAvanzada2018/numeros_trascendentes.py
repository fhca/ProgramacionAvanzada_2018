__author__ = 'fhca'

"""Generacion de numero de la forma: 1+1/(1+1/(1+1/(...)))"""


def phi(a=1): # versión iterativa
    n = 1000
    k = 1
    for i in range(n):
        k = a / (1 + k)
    return (1 + k)


def phir(a=1, i=1): # versión recursiva
    if i > 100:
        return 1 # fin de la recursividad
    else:
        return 1 + a / phir(a, i + 1)  # recursividad "de cola"


def aphi(a=1):
    n = 1000
    k = 1
    for i in range(n):
        k = 1 / (a + k)
    return (0 + k)


def nphi():
    n = 10
    k = n
    for i in range(n - 1):
        k = (n - 1 - i) / (1 + k)
    return (1 + k)


def nphir(i=1):
    if i >= 100:
        return i
    else:
        return 1 + i / nphir(i + 1)


def mphir(i=1):
    if i > 100:
        return i
    else:
        return i + 1 / mphir(i + 1)


def fibor(i=100):
    if i < 2:
        return 1
    elif i == 2:
        return 1
    else:
        return fibor(i - 1) + fibor(i - 2)

def corroboracion_de_phi():
    print("phi:", phi())
    h = 1
    for i in range(1, 35):
        k = fibor(i)
        print(i, k, k/h)
        h=k

#corroboracion_de_phi()

def fibophir(i=1):
    if i > 35:
        return 1
    else:
        return 1 + fibor(i) / fibophir(i + 1)


def fibophir2(fibo1=1, fibo2=1, i=1):
    if i > 35:
        return 1
    else:
        return 1 + fibo1 / fibophir2(fibo2, fibo1 + fibo2, i + 1)

def prueba_fibophir():
    from time import time
    t0 = time()  # time devuelve el # de seg desde 1 enero de 1970 0:00am
    print(fibophir())
    t1 = time()
    print(t1-t0)
    print(fibophir2())
    print(time() - t1)

prueba_fibophir() # fibophi(fibophir2: 0.000021934

"""
décimas             0.1 = 1 décima
centésima           0.01
milésima            0.001
diezmilésima        0.0001
cienmilésima        0.00001
millonésima         0.000001
diezmillonésima     0.0000001
cienmillonésima     0.00000001
milmillonésima      0.000000001
diezmilmillonésima  0.0000000001
cienmilmillonésima  0.00000000001
billonésima         0.000000000001
diez-
cien-
mil-
diezmil-
cienmil-
millón-
diezmillón- ...
"""

def grafica():
    import numpy as np
    import matplotlib.pyplot as plt

    x = np.arange(1000)
    plt.plot(x, aphi(x))
    plt.show()
