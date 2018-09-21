__author__ = 'fhca'

from matplotlib.pyplot import subplots, show
from matplotlib.patches import Polygon
from matplotlib.collections import PatchCollection
import numpy as np


def paso_iterativo(triangulos):
    """Da el siguiente paso en la construcción del fractal. Recibe una lista de
    vértices de triángulos y produce la lista de los vértices de los triángulos
    resultantes."""
    lista = []
    for (a, b, c) in triangulos:  # Toma uno a uno los triángulos
        ab = (a + b) / 2  # a, b, c son vértices, o sea, arreglos de 2x2.
        bc = (b + c) / 2  # En estas 3 líneas construimos los puntos medios de cada
        ca = (c + a) / 2  # lado. En la sig. línea los juntamos en triángulos.
        lista.extend([[a, ab, ca], [b, bc, ab], [c, ca, bc]])
    return np.array(lista)

def sierpinski(n):
    v = np.array([  # arreglo de triángulos, iniciando con el 1o
        [
            [0, 0],
            [1, 0],
            [.5, np.sqrt(3) / 2]
        ]
    ])

    dibujos = [Polygon(v[0])]  # guardará los dibujos (inicia con el 1er triángulo)
    # Los vértices son solo coordenadas, para que sea dibujable hay que usar Polygon
    # En la lista "dibujos" guardamos todas las figuras dibujables.
    for i in range(n):  # solo 7 iteraciones
        v1 = paso_iterativo(v)  # construye los vértices de los nuevos triángulos
        for pol in v1:
            dibujos.append(Polygon(pol))  # agrega cada triángulo (como polígono) a los dibujos
        v = v1  # actualiza el arreglo de triángulos para aplicarles un nuevo paso_iterativo

    p = PatchCollection(dibujos, alpha=.5)  # construye la colección de dibujos
    p.set_array(200 * np.random.rand(len(dibujos)))  # colores aleatorios
    fig, ax = subplots()  # área para dibujar
    ax.add_collection(p)  # añade la colección al área
    show()  # muestra lo dibujado

sierpinski(2)