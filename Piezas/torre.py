from Piezas.pieza import Pieza

class Torre (Pieza):
    def simbolo(self):
        return "♖" if self._color == "Blanco" else "♜"