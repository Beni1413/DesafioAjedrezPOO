from Piezas.peon import Peon
from Piezas.torre import Torre
from Piezas.reina import Reina
from Piezas.rey import Rey
from Piezas.caballo import Caballo
from Piezas.alfil import Alfil

class Tablero:
    def __init__(self):
        self._filas = 8
        self._columnas = 8
        self.grid = [[None for _ in range(self._columnas)] for _ in range(self._filas)]
        self.inicializar()

    def inicializar(self):
        # Peones
        for col in range(8):
            self.grid[1][col] = Peon("Blanco", (1, col))
            self.grid[6][col] = Peon("Negro", (6, col))

        self.grid[0][0] = Torre("Blanco", (0, 0))
        self.grid[0][7] = Torre("Blanco", (0, 7))
        self.grid[7][0] = Torre("Negro", (7, 0))
        self.grid[7][7] = Torre("Negro", (7, 7))

        self.grid[0][2] = Alfil("Blanco", (0, 2))
        self.grid[0][5] = Alfil("Blanco", (0, 5))
        self.grid[7][2] = Alfil("Negro", (7, 2))
        self.grid[7][5] = Alfil("Negro", (7, 5))

        self.grid[0][1] = Caballo("Blanco", (0, 1))
        self.grid[0][6] = Caballo("Blanco", (0, 6))
        self.grid[7][1] = Caballo("Negro", (7, 1))
        self.grid[7][6] = Caballo("Negro", (7, 6))


        self.grid[0][3] = Reina("Blanco", (0, 3))
        self.grid[7][3] = Reina("Negro", (7, 3))

        self.grid[0][4] = Rey("Blanco", (0, 4))
        self.grid[7][4] = Rey("Negro", (7, 4))

    def mostrar(self):
        letras_col = "  a  b  c  d  e  f  g  h"
        print("_"*27)
        print(letras_col)
        for fila in range(self._filas):
            fila_str = f"{8 - fila} "
            for col in range(self._columnas):
                pieza = self.grid[fila][col]
                fila_str += pieza.simbolo() if pieza else "."
                fila_str += "  "
            print(fila_str)
        print(letras_col)
        print("‾"*27)