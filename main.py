from tablero import Tablero

def main():
    tablero = Tablero()

    tablero.mostrar()

    letras = ['a','b','c','d','e','f','g','h']
    ficha_mover_y = str(input(f'Ingrese el valor de la columna de la pieza a mover (a-h): '))
    ficha_mover_x = int(input(f'Ingrese el valor de la fila de la pieza mover (1-8): '))
    nuevo_lugar_y = str(input(f'Ingrese el valor de la columna a donde mover la pieza (a-h): '))
    nuevo_lugar_x = int(input(f'Ingrese el valor de la fila a donde mover la pieza (1-8): '))

    col_origen = letras.index(ficha_mover_y)
    fila_origen = 8 - ficha_mover_x
    col_destino = letras.index(nuevo_lugar_y)
    fila_destino = 8 - nuevo_lugar_x

    exito = tablero.mover_pieza((fila_origen, col_origen), (fila_destino, col_destino))
    if exito:
        print("Movimiento realizado!")
    else:
        print("Ese movimiento no se puede hacer profe")
    tablero.mostrar()

if __name__ == "__main__":
    main()