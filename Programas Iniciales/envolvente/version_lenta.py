__author__ = 'fhca'


import numpy as np
from bokeh.plotting import figure, show


def izquierda(p, q, r):
    """Dice si r es un punto a la izquierda del rayo-vector determinado por pq.
    Los tres son 'puntos', arreglos uni-dimensionales de Numpy, con dos coordenadas.
    Nota: si son colineales, devuelve falso."""
    m = np.concatenate((p, q, r))
    m = np.hstack((m.reshape(3, 2), np.ones((3, 1))))
    return np.linalg.det(m) > 2e-15  # margen de error


def izquierda2(p, q, r):
    """Modificación para detectar puntos colineales"""
    m = np.concatenate((p, q, r))
    m = np.hstack((m.reshape(3, 2), np.ones((3, 1))))
    margen_de_error = 2e-15
    determinante = np.linalg.det(m)
    if determinante > margen_de_error:
        return +1
    elif determinante < -margen_de_error:
        return -1
    else:
        return 0


def genera_puntos(tamano):
    """generea un arreglo de 'tamano' puntos al azar."""
    return np.random.randn(tamano * 2).reshape(tamano, 2) * 100


def muestra_puntos(p, f="nada"):
    if f == "nada":
        f = figure()
    f.circle(*p.T)
    show(f)
    return f


def dif(p, q):
    """Son diferentes los puntos p y q?."""
    return p[0] != q[0] or p[1] != q[1]


def envolvente_lenta(puntos):
    """Determina las aristas de la envolvente convexa del conjunto de 'puntos' p"""
    _e = np.array([])
    for p in puntos:
        for q in puntos:
            if dif(p, q):
                valida = True
                for r in puntos:
                    if dif(p, r) and dif(q, r):
                        if izquierda(p, q, r):
                            valida = False
                            break
                if valida:
                    _e = np.concatenate((_e, p, q))
    return _e


def ordena(e):
    """Ordena horariamente los extremos de arista en e. Versión super lenta."""
    env = []
    p, q = e[0]
    env.append(p)
    while dif(q, p):
        for a, b in e:
            if not dif(a, q):
                env.append(q)
                q = b
                break
    env.append(p)
    return np.array(env)


p = genera_puntos(80)
f = muestra_puntos(p)
e = envolvente_lenta(p).reshape(-1, 2, 2)  # todas las aristas constan de dos coord de dos puntos
o = ordena(e)
f.line(*o.T, color="red")
show(f)
