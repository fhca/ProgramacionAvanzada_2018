import matplotlib.pyplot as plt
import numpy as np

f = plt.figure(figsize=(5, 5))
f.add_subplot(111)


def circulo(a=0, b=0, radio=1):
    n = 100
    angulo = np.linspace(0, 2 * np.pi, n)
    x = radio * np.cos(angulo) + a
    y = radio * np.sin(angulo) + b
    plt.plot(x, y, '-')


def rojo(a, b, radio, angulo):
    x = radio * np.cos(angulo) + a
    y = radio * np.sin(angulo) + b
    plt.plot(x, y, 'o', color='red')


circulo(0, 0, 10)
circulo(-3, 3, 2)  # ojo izq
circulo(3, 3, 2)  # ojo der
rojo(-3, 3, 2, 3 * np.pi / 2)
rojo(3, 3, 2, 0)

#orejas
rojo(0,0, 10, 3*np.pi/4)
rojo(0,0, 10, np.pi/4)

plt.show()
