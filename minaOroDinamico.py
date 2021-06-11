# Se encarga de resolver el problema de la mina de oro con el método dinámico
def minaOroDinamico(matrizMina, filas,columnas):
    matrizMaximosCostos=[[0 for i in range(columnas)] for j in range(filas)]
    for i in range(filas) :
        matrizMaximosCostos[i][0] = matrizMina[i][0]

    for j in range (1,columnas):
        for i in range(filas):
            matrizMaximosCostos[i][j] = matrizMina[i][j]#Valor original
            costoMax = matrizMaximosCostos[i][j - 1]  #maximo valor hacia la izquierda
            if i - 1 >= 0:
                if costoMax < matrizMaximosCostos[i - 1][j - 1]:  #compara el valor izquierdo con la diagonal arriba izquierda
                    costoMax = matrizMaximosCostos[i - 1][j - 1]
            if i + 1 < filas:
                if costoMax < matrizMaximosCostos[i + 1][j - 1]:  #compara el valor izquierdo con la diagonal abajo izquierda immediate left to left lower diagonal
                    costoMax = matrizMaximosCostos[i + 1][j - 1]
            matrizMaximosCostos[i][j] += costoMax             # añadir el maximo al valor izquierdo

    #Selecciona el máximo de la ultima lista para sacar el maximo de oro que se puede sacar de la mina
    resultado = matrizMaximosCostos[0][columnas - 1]
    for i in range(0 , filas):
        if matrizMaximosCostos[i][columnas - 1] > resultado:
            resultado = matrizMaximosCostos[i][columnas - 1]

    return resultado

