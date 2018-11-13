__author__ = 'fhca'

texto = "El respeto al derecho ajeno es la paz."

# print("Texto original:", texto)


def cifrado_cesar(texto, password):
    return "".join([chr(ord(c) + password) for c in texto])


# cifrado = cifrado_cesar(texto, 3)
#
# print("Texto cifrado:", cifrado)


##########  AL RECIBIRLO  #########


def descifrado_cesar(texto, password):
    # return "".join([chr(ord(c) - 3) for c in texto])
    return cifrado_cesar(texto, -password)


# for despl in range(10):
#     print(despl, "Texto descifrado:", descifrado_cesar(cifrado, despl))

tabla = {"a": " tierra", "b": " raiz", "c": " flor", "d": " abeja", "e": " ahora",
         "l": " de", "r": " aqui", "p": " viento", "t": " el", "j": " sol", "z": " polen",
         ".": " en", "o": " nube", "s": " rapido", "E": " reina",
         "n": " porque", "h": " cuando", " ": " y "}  # sustitución

# for c in texto:
#     print(tabla[c], end="")


# "esteganografía" + "esconder algo a plena vista"

"RansomWare"


# mes fecha hora cajero sucursal ciudad banco cantidad
# 1111111111001101101110000
# 2222222222112212212221111  # sumale uno
# 22 22 22 22 22 11 22 12 21 22 21 11 1  # juntalos en parejas
# 44 44 42 43 34 32 1  # suma los dígitos de cada pareja
# 8867751 # separa en parejas y suma los dígitos de cada pareja


# 3 6 5
def cifrado_cesar_avanzado(texto, password):
    """password es una lista de números que se cicla."""
    actual = 0
    l = []
    texto = texto.lower()
    for c in texto:
        l.append(chr(ord(c) + password[actual]))
        actual = (actual + 1) % len(password)
    return "".join(l)


cifrado=cifrado_cesar_avanzado("cuidado con los gatos, que pueden ser traicioneros.", [3, 6000000, 5])

print(cifrado)

def descifrado_cesar_avanzado(texto, password):
    neg = [-p for p in password]
    return cifrado_cesar_avanzado(texto, neg)

print(descifrado_cesar_avanzado(cifrado, [3,6000000,5]))