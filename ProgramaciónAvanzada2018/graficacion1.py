__author__ = 'fhca'

from numpy import sin, pi, log
# Bibliotecas para graficar: tkinter, matplotlib, bokeh

import matplotlib.pyplot as plt


def f(x):
    return sin(x)


def graficar(intervalo, función, tamaño=100):
    delta_x = (intervalo[1] - intervalo[0]) / (tamaño - 1)
    x = intervalo[0]

    xs = []
    ys = []
    for i in range(tamaño):
        # print(i, x, función(x))
        xs.append(x)
        ys.append(función(x))
        x += delta_x  # otra forma: x = x + delta_x

    # print(xs)
    # print(ys)
    plt.figure()  # inicializa el espacio para graficar
    plt.plot(xs, ys)  # como queremos que lo grafique
    plt.show()  # muestra la gráfica


# definamos el intervalo en que localizaremos a las x
# min_intervalo = -2*pi
# max_intervalo = 2*pi
graficar([0, 4 * pi], f)


def g(x):
    return x ** 3


graficar([-100, 100], g)

graficar([-2, 2], lambda x: sin(1 / x), 10000)

graficar([-10, 10], lambda x: log(x ** 2), 1000)

graficar([-1, 1], lambda x: sin(1 / x ** 2), 10000)
