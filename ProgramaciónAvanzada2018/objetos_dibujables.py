__author__ = 'fhca'

class Dibujable:
    def __init__(self):
        self.posicion = np.random.rand(2)  # posición son dos coord. al azar

    def pinta(self):
        pass  # no pondré las operaciones en este momento

    def mueve_a_xy(self, x, y):
        """Mueve el objeto a la posición (x,y)."""
        self.posicion = np.array((x, y))

