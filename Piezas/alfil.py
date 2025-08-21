from Piezas.pieza import Pieza
class Alfil(Pieza):
    def simbolo(self):
        return "♗" if self._color == "Blanco" else "♝"
