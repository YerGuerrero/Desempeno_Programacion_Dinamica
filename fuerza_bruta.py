

# Se encarga de resolver el problema de la mochila con el método fuerza bruta
def fuerza_bruta(pesoMaximo, listaPesos, listasGanancias, n):
    if n == 0 or pesoMaximo == 0:
        return 0

    if (listaPesos[n - 1] > pesoMaximo):
        return fuerza_bruta(pesoMaximo, listaPesos, listasGanancias, n - 1)

    else:
        return max(listasGanancias[n - 1] + fuerza_bruta(
                pesoMaximo - listaPesos[n - 1], listaPesos, listasGanancias, n - 1),
            fuerza_bruta(pesoMaximo, listaPesos, listasGanancias, n - 1))