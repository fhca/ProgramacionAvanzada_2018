__author__ = 'fhca'

import matplotlib.pyplot as plt

import numpy as np


def leer_archivo():
    with open(r"MMAS550429VIGREP_F3.txt") as f:
        lista = f.readlines()
    ys = [float(elemento) for elemento in lista]
    return np.array(ys)


def graficar(ys):
    xs = range(len(ys))
    print(len(ys))
    plt.figure()
    plt.plot(xs, ys, linewidth=.1)
    #plt.savefig("F3.png", dpi=500)


ys = leer_archivo()

print("Num de valores mayores que 1:", (ys > 1).sum())
print("Num de valores menores que -5:", (ys < -5).sum())

ys[ys > 1] = 1.0
ys[ys < -5] = -5.0

print("Num de valores mayores que 1:", (ys > 1).sum())
print("Num de valores menores que -5:", (ys < -5).sum())


# ys = ys[50000:150000]  # subintervalo
graficar(ys)
plt.ylim((-20,30))
# plt.hist(ys, 100)  # 100 bins
plt.show()
