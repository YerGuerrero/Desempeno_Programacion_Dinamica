cont=0
mejorMochila=[]
mejorValor=0

def fuerza_bruta(pesoMaximo, listaPesos, listasGanancias, n):
    global cont
    mochilaActual = []

    if n == 0 or pesoMaximo == 0:
        return 0

    if (listaPesos[n - 1] > pesoMaximo):
        cont += 1
        return fuerza_bruta(pesoMaximo, listaPesos, listasGanancias, n - 1)

    else:
        cont+=1
        mochilaActual.append(cont)
        m=max(
            listasGanancias[n - 1] + fuerza_bruta(
                pesoMaximo - listaPesos[n - 1], listaPesos, listasGanancias, n - 1),
            fuerza_bruta(pesoMaximo, listaPesos, listasGanancias, n - 1))
        mejorMochila=mochilaActual
        print(mejorMochila)
        return m
