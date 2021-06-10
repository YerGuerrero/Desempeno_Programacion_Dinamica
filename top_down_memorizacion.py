
# Se encarga de resolver el problema de la mochila con el método top down
def top_down(pesoMaximo, listaPesos, listasGanancias, n):
    mem = [[-1 for i in range(pesoMaximo + 1)] for j in range(n + 1)]
    return top_down_aux(mem, listaPesos, listasGanancias, pesoMaximo, n)

# Función que mantiene la recursión
def top_down_aux(mem, listaPesos, listasGanancias, pesoMaximo, n):

    if n == 0 or pesoMaximo == 0:
        return 0
    if mem[n][pesoMaximo] != -1:
        return mem[n][pesoMaximo]

    if listaPesos[n - 1] <= pesoMaximo:
        mem[n][pesoMaximo] = max(
            listasGanancias[n - 1] + top_down_aux(mem, listaPesos, listasGanancias, pesoMaximo - listaPesos[n - 1], n - 1),
            top_down_aux(mem, listaPesos, listasGanancias, pesoMaximo, n - 1))
        return mem[n][pesoMaximo]
    elif listaPesos[n - 1] > pesoMaximo:
        mem[n][pesoMaximo] = top_down_aux(mem, listaPesos, listasGanancias, pesoMaximo, n - 1)
        return mem[n][pesoMaximo]
