class Pieza:
    def __init__(self, color, posicion):
        self._color = color
        self._posicion = posicion
    
    def moverse(self, nueva_posicion, tablero):
        self.posicion = nueva_posicion
    
    def simbolo(self):
        return "?"