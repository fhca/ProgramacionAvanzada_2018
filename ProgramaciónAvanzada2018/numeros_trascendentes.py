__author__ = 'fhca'

"""Generación de número de la forma: 1+1/(1+1/(1+1/(...)))"""


def phi(a=1):
    n = 1000
    k = 1
    for i in range(n):
        k = a / (1 + k)
    return (1 + k)


def aphi(a=1):
    n = 1000
    k = 1
    for i in range(n):
        k = 1 / (a + k)
    return (0 + k)


def nphi():
    n = 1000
    k = n
    for i in range(n - 1):
        k = (n - 1 - i) / (1 + k)
    return (1 + k)


print(nphi())


def grafica():
    import numpy as np
    import matplotlib.pyplot as plt

    x = np.arange(1000)
    plt.plot(x, aphi(x))
    plt.show()
