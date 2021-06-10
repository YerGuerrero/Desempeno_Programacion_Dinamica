cont=0
mejorMochila=[]
mejorValor=0

# Se encarga de resolver el problema de la mochila con el método fuerza bruta
def fuerza_bruta(pesoMaximo, listaPesos, listasGanancias, n):
    global cont
    mochilaActual = []
    print(listaPesos)
    print(listasGanancias)
    print(cont)
    if n == 0 or pesoMaximo == 0:
        return 0

    if (listaPesos[n - 1] > pesoMaximo):
        cont += 0
        return fuerza_bruta(pesoMaximo, listaPesos, listasGanancias, n - 1)

    else:
        cont+=1
        mochilaActual.append(listasGanancias[cont])
        m=max(listasGanancias[n - 1] + fuerza_bruta(
                pesoMaximo - listaPesos[n - 1], listaPesos, listasGanancias, n - 1),
            fuerza_bruta(pesoMaximo, listaPesos, listasGanancias, n - 1))
        mejorMochila=mochilaActual

        return m
