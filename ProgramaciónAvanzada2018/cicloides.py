__author__ = 'fhca'

import matplotlib.pyplot as plt
import matplotlib.colors as colors
import matplotlib.cm as cmx
import numpy as np

f = plt.figure()
#f.add_subplot(111)
plt.axis('equal')


def circulo(a=0, b=0, radio=1):
    n = 100
    angulo = np.linspace(0, 2 * np.pi, n)
    x = radio * np.cos(angulo) + a
    y = radio * np.sin(angulo) + b
    plt.plot(x, y, '-')


def cicloide(a=0, b=0, radio=1, angulo=0):
    x = radio * np.cos(3 * np.pi / 2 - angulo) + a
    y = radio * np.sin(3 * np.pi / 2 - angulo) + b
    # plt.plot(x, y, 'o', color='red')
    return x, y


def hipocicloide(r=1, R=1, colores=100):
    ainic = 0
    #mapa = cm = plt.get_cmap('ocean')
    mapa = cm = plt.get_cmap('hsv')
    cNorm = colors.Normalize(vmin=0, vmax=colores)
    scalarMap = cmx.ScalarMappable(norm=cNorm, cmap=mapa)
    for _ in range(colores):
        t = np.linspace(ainic, ainic + 2 * np.pi, 1000)
        ainic += 2 * np.pi
        a, b = cicloide(radio=R - r, angulo=t)
        tp = -t * (R - r) / r
        # plt.plot(a, b, '.')
        ap, bp = cicloide(a, b, r, tp)

        colorVal = scalarMap.to_rgba(_)
        plt.plot(ap, bp, linewidth=.5, color=colorVal)


hipocicloide(r=6)
#hipocicloide(R=4.01)

plt.show()
