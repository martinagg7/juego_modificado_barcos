from clases.Tablero import Tablero
from clases.Barco import Barco
from Conventions import *


class Casilla:
    instances = {}
    jugadas = set()

    def __init__(self, x, y):
        # Adición de las coordenadas
        self.x = x
        self.y = y
        # Queremos poder acceder a una casilla a partir de sus coordenadas
        self.__class__.instances[x, y] = self

        # Generación del nombre de la casilla
        self._generar_nombre()
        # Queremos poder acceder a una casilla a partir de su nombre
        self.__class__.instances[self.nombre] = self

        # Evolución de la casilla
        self.jugada = False
        self.barco = None  # No toca a un barco de momento.

    def _generar_nombre(self):
        """Este método puede ser sobrecargado fácilmente"""
        self.nombre = generar_nombre_casilla(self.x, self.y)

    def jugar(self):
        """Describe qué pasa cuando jugamos una casilla"""
        self.jugada = True
        self.__class__.jugadas.add(self)

        if self.barco is not None:
            if len(self.barco.casillas - self.__class__.jugadas) == 0:
                print("El barco ha sido hundido !!")
            else:
                print("El barco ha sido tocado !")
        else:
            print("Agua !")

    @classmethod
    def generar_casillas(cls):
        for x, y in product(range(Tablero.num_lineas),
                            range(Tablero.num_columnas)):
            cls(x, y)

    def __str__(self):
        """Sobrecarga del método de transformación en cadena"""
        if not self.jugada:
            return "Casilla no jugada"
        elif self.barco is None:
            return "Agua"
        return "Casilla tocada"
