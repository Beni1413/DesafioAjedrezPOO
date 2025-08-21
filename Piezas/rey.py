from Piezas.pieza import Pieza

class Rey (Pieza):
    def simbolo(self):
        return "♔" if self._color == "Blanco" else "♚"