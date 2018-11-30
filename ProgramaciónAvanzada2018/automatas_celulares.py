__author__ = 'fhca'

import numpy as np

e = np.zeros((130, 130), dtype=bool)

# e[0, 1] = e[0, 3] = e[0, 4] = e[0, 5] = e[0, 8] = e[0, 11] = 1

e[0] = np.random.randint(0, 2, e.shape[1])

""" 
e[5, -1]  <-- no es error, es la última columna
e[5, 13]  <-- error!, no hay columna 13
"""


def celda(e, i, j, regla):
    """pone el valor 0 o 1 dependiendo de f,
    en la celda renglón i, columna j."""
    nrenglones, ncolumnas = e.shape
    if j >= ncolumnas - 1:  # num de columnas
        e[i, j] = f(e[i - 1, j - 1], e[i - 1, j], e[i - 1, 0], regla)
    else:
        e[i, j] = f(e[i - 1, j - 1], e[i - 1, j], e[i - 1, j + 1], regla)


def f(x, y, z, regla):
    return binario(regla)[4 * x + 2 * y + z]  # Esto sería más rápido x<<2|y<<1|z


def binario(n):
    "numero de regla en binario, volteado"
    bina = []
    while n >= 1:
        n, residuo = divmod(n, 2)
        bina.append(residuo)
    size = len(bina)
    if size < 8:
        bina.extend([0] * (8 - size))
    return bina


""" # Esta versión es más rápida porque NO TIENE CICLOS!!! (explícitos)
def binario2(n):
    bina = bin(n)  # las operaciones matemáticas están implícitas aquí
    regla_traducida = bina[2:].zfill(8)[::-1]
    return int(regla_traducida)
"""


def aplica_autómata(e, regla):
    nrenglones, ncolumnas = e.shape
    for i in range(1, nrenglones):
        for j in range(ncolumnas):
            celda(e, i, j, regla)
    import matplotlib.pyplot as plt
    plt.imshow(e)
    plt.show()


aplica_autómata(e, 120)
