
class Pieza:
    def __init__(self, color, posicion):
        self._color = color
        self._posicion = posicion
    
    def simbolo(self):
        return "?"