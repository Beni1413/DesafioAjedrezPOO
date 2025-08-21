from Piezas.pieza import Pieza

class Reina (Pieza):
    def simbolo(self):
        return "♕" if self._color == "Blanco" else "♛"