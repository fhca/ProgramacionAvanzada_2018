__author__ = 'fhca'


def busca_letra1(letra, cadena):
    """Dice si una letra está en una cadena."""
    for una_letra in cadena:
        if letra == una_letra:
            return True  # Devuelve True tan pronto la encuentre
    return False  # Si termina y nunca devolvió True, es que no estaba. Devuelve False


print("Ejemplo 1")
if busca_letra1("j", "El respeto al derecho ajeno es la paz."):
    print("Si está")
else:
    print("No está")


def busca_letra2(letra, cadena):
    """Dice si una letra está en una cadena."""
    return (letra.lower() in cadena) or (letra.upper() in cadena)


print("Ejemplo 2")
if busca_letra2("i", "La patria es primero."):
    print("Si está")
else:
    print("No está")


def busca_letras1(letras, texto):
    """Dice si la secuencia de letras se encuentra contigua en el texto dado. NO FUNCIONA."""
    iletras = 0  # indice actual en las letras
    itexto = 0  # indice actual en el texto
    lletras = len(letras)  # longitud de las letras
    ltexto = len(texto)  # longitud del texto
    while itexto < ltexto:
        if letras[iletras] == texto[itexto]:
            iletras += 1
        else:
            iletras = 0
        if iletras == lletras:
            return True
        itexto += 1
    return False


print("Ejemplo 3")
if busca_letras1("sobre", "Mas vale que sosobre y no que fafalte."):
    print("Si está")
else:
    print("No está")


def busca_letras2(letras, texto):
    """Dice si la secuencia de letras se encuentra contigua en el texto dado."""
    iletras = 0  # indice actual en la palabra
    itexto = 0  # indice actual en el texto
    lletras = len(letras)  # longitud de la palabra
    ltexto = len(texto)  # longitud del texto
    regreso = 0
    while itexto < ltexto:
        if letras[iletras] == texto[itexto]:
            if iletras == 1:
                regreso = itexto
            iletras += 1
            itexto += 1
        else:
            if iletras > 1:
                itexto = regreso
                iletras = 0
            else:
                itexto += 1
        if iletras == lletras:
            return True
    return False


print("Ejemplo 4")
if busca_letras2("sobre", "Mas vale que ssssobre y no que fafalte."):
    print("Si está")
else:
    print("No está")
