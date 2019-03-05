__author__ = 'fhca'

"""
LISTAS LIGADAS

Una lista es una estructura de datos "sencilla". En su forma mas
simple un nodo contiene un dato a guardar y la "forma" de llegar
a otro nodo (el "siguiente"). ADEMAS es necesario conocer el nodo
inicial (raiz) de la lista, a fin de poder llegr a todos los demás
nodos.

Algoritmos:

crear_nodo(dato) - reserva espacio para el nodo e indica que
                        el siguiente nodo será None.

guardar(dato, lista) - Si la lista no existe, entonces su raiz será
                        el nodo resultante de crear_nodo(dato)
                        
                        En caso de que si exista la lista:
                        nodo = raiz  (es diferente de None)
                        mientras nodo tenga un siguiente:
                            nodo = siguiente
                        de lo contrario:
                            ultimo = nodo
                        el siguiente del ultimo será el nodo resultante
                        de crear_nodo(dato)
                        
mostrar(lista) - Si la lista no está vacía:
                    nodo = raiz
                    mientras nodo tenga un siguiente:
                        muestra el dato del nodo
                        nodo = siguiente
                    de lo contrario
                        muestra el dato del último nodo

buscar(dato, lista) - Si la lista no está vacía:
                nodo = raiz
                mientras nodo tenga un siguiente:
                    verifica si dato = dato del nodo
                    SI: termina diciendo que lo encontró
                    NO: nodo = siguiente
                de lo contrario:
                    verifica si dato = dato del nodo
                    SI: termina diciendo que lo encontró
                    NO: termina diciendo que no lo encontró
"""

class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

    def muestra(self):
        print(self.dato)

class Lista:
    def __init__(self):
        self.raiz = None

    def esta_vacía(self):
        "True = lista vacía"
        return self.raiz is None

    def guardar(self, dato):
        if self.esta_vacía():
            self.raiz = Nodo(dato)  # crear_nodo
        else:
            nodo = self.raiz
            while nodo.siguiente:
                nodo = nodo.siguiente
            ultimo = nodo
            ultimo.siguiente = Nodo(dato)

    def mostrar(self):
        nodo = self.raiz
        while nodo.siguiente:
            nodo.muestra()
            nodo = nodo.siguiente
        nodo.muestra()

    def buscar(self, dato):
        nodo = self.raiz
        while nodo.siguiente:
            if dato == nodo.dato:
                return True
            else:
                nodo = nodo.siguiente
        if dato == nodo.dato:
            return True
        else:
            return False

def pruebas_Lista():
    l = Lista()
    l.guardar("Paty")  # guarda el dato "Paty" en la lista l
    l.guardar("Samuel")
    l.guardar("Uriel")
    l.guardar("David")
    l.guardar("Max")
    l.guardar("Abraham")
    l.guardar("Angel")
    l.mostrar()

    if l.buscar("Samuel"):
        print("Si está Samuel")
    else:
        print("No está Samuel")

"""
Para guardar 7 datos, tuve que usar 28 pasos!!! 7*8/2 n(n+1)/2 = O(n^2)
"""

"""
Modificación para guardar siempre el último
"""

class Lista2:
    def __init__(self):
        self.raiz = None
        self.último = None

    def esta_vacía(self):
        "True = lista vacía"
        return self.raiz is None

    def guardar(self, dato):
        if self.esta_vacía():
            self.último = self.raiz = Nodo(dato)  # crear_nodo
        else:
            ultimo = self.último
            ultimo.siguiente = Nodo(dato)
            self.último = ultimo.siguiente

    def mostrar(self):
        nodo = self.raiz
        while nodo.siguiente:
            nodo.muestra()
            nodo = nodo.siguiente
        nodo.muestra()

    def buscar(self, dato):
        nodo = self.raiz
        while nodo.siguiente:
            if dato == nodo.dato:
                return True
            else:
                nodo = nodo.siguiente
        if dato == nodo.dato:
            return True
        else:
            return False

"""Con esto se reduce la complejidad temporal de 'guardar' de O(n^2) a O(1)"""

def pruebas_Lista2():
    l = Lista2()
    l.guardar("Paty")  # guarda el dato "Paty" en la lista l
    l.guardar("Samuel")
    l.guardar("Uriel")
    l.guardar("David")
    l.guardar("Max")
    l.guardar("Abraham")
    l.guardar("Angel")
    l.mostrar()


class Nodo_arbol:
    def __init__(self, dato):
        self.dato = dato
        self.izq = None
        self.der = None

    def muestra(self):
        print(self.dato)

class Arbol:
    """Árbol binario, no necesariamente balanceado."""
    def __init__(self):
        self.raiz = None

    def esta_vacío(self):
        "True = árbol vacío"
        return self.raiz is None

    def guardar(self, dato):
        if self.esta_vacío():
            self.raiz = Nodo_arbol(dato)
        else:
            self.guarda_en_subarbol(dato, self.raiz)

    def guarda_en_subarbol(self, dato, nodo):
        """Toma nodo como raiz del subarbol e intenta guardar ahí el dato."""
        if dato < nodo.dato:
            if nodo.izq:
                self.guarda_en_subarbol(dato, nodo.izq)
            else:
                nodo.izq = Nodo_arbol(dato)
        else:
            if nodo.der:
                self.guarda_en_subarbol(dato, nodo.der)
            else:
                nodo.der = Nodo_arbol(dato)

    def mostrar(self):
        """Recorrido "in-orden" (IRD) del árbol."""
        self.muestra_ird(self.raiz)

    def muestra_ird(self, raiz):
        if raiz:
            if raiz.izq:
                self.muestra_ird(raiz.izq)
            raiz.muestra()
            if raiz.der:
                self.muestra_ird(raiz.der)

def prueba1_arbol():
    a = Arbol()
    a.guardar(4)
    a.guardar(2)
    a.guardar(6)
    a.guardar(1)
    a.guardar(3)
    a.guardar(5)
    a.guardar(7)
    a.mostrar()

def prueba2_arbol():
    a = Arbol()
    a.guardar("Abraham")
    a.guardar("Max")
    a.guardar("Uriel")
    a.guardar("David")
    a.guardar("Samuel")
    a.guardar("Paty")
    a.guardar("Claudia")
    a.guardar("Botitas")
    a.guardar("Suky")
    a.guardar("Felipe")
    a.mostrar()


prueba2_arbol()