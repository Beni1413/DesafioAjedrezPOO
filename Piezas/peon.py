from Piezas.pieza import Pieza

class Peon (Pieza):
    def simbolo(self):
        return "♙" if self._color == "Blanco" else "♟"

    def moverse(self, nueva_posicion, tablero):
        fila_actual, col_actual = self._posicion
        fila_nueva, col_nueva = nueva_posicion
        print(f"Tu movimiento fue: color={self._color}, actual=({fila_actual},{col_actual}), nueva=({fila_nueva},{col_nueva})")
        if self._color == "Blanco":
            if col_nueva == col_actual and fila_nueva == fila_actual + 1:
                self._posicion = nueva_posicion
                return True
        else:
            if col_nueva == col_actual and fila_nueva == fila_actual - 1:
                self._posicion = nueva_posicion
                return True
        return False

