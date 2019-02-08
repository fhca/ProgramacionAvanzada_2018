__author__ = 'fhca'


class ObjetoGeometrico:
    """Describir las cosas comunes (acciones y características)
    a los objetos geométricos."""

    def __init__(self, como_se_llama="Objeto geométrico", planeta="Tierra"):
        """Constructor. Es lo primero que se ejecuta al instanciar el objeto. (crearlo)"""
        self.pon_nombre(como_se_llama)
        self.planeta = planeta

    def dame_nombre(self):
        """Devuelve el nombre del objeto actual."""
        return self.mi_nombre

    def pon_nombre(self, nom):
        """Modifica el nombre del objeto actual."""
        self.mi_nombre = nom

    def dame_info(self, nombre_de_la_variable):
        """Imprime información útil sobre el objeto actual."""
        print("Objeto", nombre_de_la_variable)
        print("Nombre:", self.dame_nombre())
        print("Planeta", self.planeta)
        print("Área", self.area())
        print("Perimetro", self.perimetro())

    def area(self):
        pass

    def perimetro(self):
        pass


if __name__ == "__main__":
    x = ObjetoGeometrico()
    y = ObjetoGeometrico(planeta="Júpiter")
    z = ObjetoGeometrico("Samuelito")

    planeta = "Venus"
    x.dame_info("x")
    y.dame_info("y")

    x.pon_nombre("Pedrito")
    y.pon_nombre("Lalita")

    x.dame_info("x")
    y.dame_info("y")
    z.dame_info("z")
