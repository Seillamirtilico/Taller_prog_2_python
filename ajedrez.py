filaPartida = int(input("Introduce la fila de partida (1-8): "))
columnaPartida = int(input("Introduce la columna de partida (1-8): "))
movimientosCaballo = [
    [-2, -1], [-2, 1],
    [-1, -2], [-1, 2],
    [1, -2], [1, 2],
    [2, -1], [2, 1]
]
if filaPartida >= 1 and filaPartida <= 8 and columnaPartida >= 1 and columnaPartida <= 8:
    print("Posiciones a las que puede moverse el caballo:")
    for i in range(len(movimientosCaballo)):
        nuevaFila = filaPartida + movimientosCaballo[i][0]
        nuevaColumna = columnaPartida + movimientosCaballo[i][1]
        if nuevaFila >= 1 and nuevaFila <= 8 and nuevaColumna >= 1 and nuevaColumna <= 8:
            print("({}, {})".format(nuevaFila, nuevaColumna))
else:
    print("La posición ingresada no es válida.")
