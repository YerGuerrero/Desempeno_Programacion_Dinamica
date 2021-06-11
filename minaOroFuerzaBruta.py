
# Resuelve el problema de la mina de oro con el metodo fuerza bruta
def minaOroFuerzaBruta(matrizMina, filas, columnas):

    matrizOro = [[0 for i in range(columnas)] for j in range(filas)]# Matriz en donde se van a mantener los maximos de oros
    matrizMaximos=[]
    maximos=[]

    for columna in range(columnas - 1, -1, -1):
        maximos = []
        for fila in range(filas):

            if (columna == columnas - 1):
                derecha = 0
            else:
                derecha = matrizOro[fila][columna + 1]# Revisa la celda a la derecha

            if (fila == 0 or columna == columnas - 1):
                diagonalArriba = 0
            else:
                diagonalArriba = matrizOro[fila - 1][columna + 1]# Revisa la diagonal arriba

            if (fila == filas - 1 or columna == columnas - 1):
                diagonalAbajo = 0
            else:
                diagonalAbajo = matrizOro[fila + 1][columna + 1]# Revisa la diagonal abajo

            maximos.append([max(derecha, diagonalArriba, diagonalAbajo),matrizMina[fila][columna]])# Se saca el maximo de oro recolectado de cualquiera de los caminos
            matrizOro[fila][columna] = matrizMina[fila][columna] + max(derecha, diagonalArriba, diagonalAbajo)
        matrizMaximos.append(maximos)

    resultado = matrizOro[0][0]
    for i in range(1, filas):
        resultado = max(resultado, matrizOro[i][0])
    return resultado