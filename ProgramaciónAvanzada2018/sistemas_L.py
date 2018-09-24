__author__ = 'fhca'

import numpy as np
from matplotlib.pyplot import figure, show, plot


def itera(cad, reglas, n):
    """Itera el sistema con cad como cadena inicial usando las reglas, n veces"""
    for i in range(n):
        cad = "".join([reglas.get(s, s) for s in cad])  # si no encuentra s, lo repite, tal cual
    return cad


def pinta(cad):
    posicion = np.array([0, 0])  # centro
    angulo = 0
    escala = 1  # longitud del paso
    lista = [posicion]
    dibujo = [lista]  # lista de dibujos
    estados = []  # pila de estados posicion, angulo, escala
    for s in cad:
        if s == 'F' or s == 'A' or s == 'B':
            posicion = posicion + escala * np.array((np.cos(angulo), np.sin(angulo)))
            lista.append(posicion)
        if s == 'K':
            posicion = posicion - escala * np.array((np.cos(angulo), np.sin(angulo)))
            lista.append(posicion)
        if s == '(':
            escala /= 2
        if s == ')':
            escala *= 2
        if s == '[':  # almacena estado
            lista = [posicion]  # crea una nueva lista de posiciones, inicia en la actual
            dibujo.append(lista)  # la agrega al dibujo
            estados.append([posicion, angulo, escala])  # guarda estado actual
        if s == "]":  # recupera último estado almacenado
            lista = []  # crea una nueva lista de vertices
            dibujo.append(lista)  # la agrega al dibujo
            posicion, angulo, escala = estados.pop()  # recupera el último estado guardado
            lista.append(posicion)  # continua el dibujo desde donde se quedó
        if s == "<":  # 60º
            angulo += np.pi / 3
        if s == ">":
            angulo -= np.pi / 3
        if s == "+":  # 90º
            angulo += np.pi / 2
        if s == "-":
            angulo -= np.pi / 2
        if s == "L":  # 10º
            angulo += np.pi / 18
        if s == "R":
            angulo -= np.pi / 18
    figure()
    for lista in dibujo:
        lista = np.array(lista).T
        plot(*lista)
    show()


koch = ["F", {"F": "F<F>>F<F"}]
koch2 = ["F", {"F": "F+F-F-F+F"}]
sierpinsky = ["<F>>F>>F>>", {"F": "(F>>F>>F>>)F"}]
sierpinsky2 = ["A", {"A": "B>A>B", "B": "A<B<A"}]  # pares e impares
rama = ["+F", {"F": "F[RRF][LLLFF]"}]
rama2 = ["+F", {"F": "F[-F]F[+F][F]"}]
rama3 = ["+F", {"F": "F[RF]F[LF]"}]
rama4 = ["+F", {"F": "F[(+F)][(-F)]"}]
rama5 = ["+F", {"F": "F[LLLF][LF]"}]
sierpinsky3 = ["A", {"A": "BRARB", "B": "ALBLA"}]

ls = itera(*sierpinsky, 1)
pinta(ls)
