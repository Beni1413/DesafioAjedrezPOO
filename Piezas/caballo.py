from Piezas.pieza import Pieza
class Caballo(Pieza):
    def simbolo(self):
        return "♘" if self._color == "Blanco" else "♞"
