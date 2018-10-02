__author__ = 'fhca'

import re


def estadisticas(libro):
    with open(libro) as f:
        t = f.readlines()

    words = re.compile(r'\W+')
    dots = re.compile(r'\.')

    megalista = []
    for parrafo in t:
        p = parrafo.lower()  # pasa a minúsculas el párrafo
        megalista.extend(dots.split(p))

    ha = he = ro = hr = hh = 0
    for p in megalista:
        if "harry" in p:
            ha += 1
        if "hermione" in p:
            he += 1
        if "ron" in p:
            ro += 1
        if ("hermione" in p) and ("harry" in p) and not ("ron" in p):
            hh += 1
        if ("hermione" in p) and ("ron" in p) and not ("harry" in p):
            hr += 1

    print("---Estadisticas del libro: {}---".format(libro))
    print("Hermione:", he)
    print("Ron:", ro)
    print("Harry:", ha)
    print("parrafos con Hermione + Ron =", hr)
    print("parrafos con Hermione + Harry =", hh)
    print("Preferencia de Hermione por Ron vs Harry", hr/hh)


estadisticas("textos/L1piedra.txt")
estadisticas("textos/L2camara.txt")
estadisticas("textos/L3azkaban.txt")
estadisticas("textos/L4caliz.txt")