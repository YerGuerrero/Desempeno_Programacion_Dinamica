def bottom_up(pesoMaximo, listaPesos, listasGanancias, n):
    matriz = [[0 for x in range(pesoMaximo + 1)] for x in range(n + 1)]

    # Build table K[][] in bottom up manner
    for i in range(n + 1):
        for j in range(pesoMaximo + 1):
            if i == 0 or j == 0:
                matriz[i][j] = 0
            elif listaPesos[i - 1] <= j:
                matriz[i][j] = max(listasGanancias[i - 1]
                              + matriz[i - 1][j - listaPesos[i - 1]],
                              matriz[i - 1][j])
            else:
                matriz[i][j] = matriz[i - 1][j]
    return matriz[n][pesoMaximo]
