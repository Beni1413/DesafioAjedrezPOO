from Piezas.pieza import Pieza
class Peon (Pieza):
    def simbolo(self):
        return "♙" if self._color == "Blanco" else "♟"
