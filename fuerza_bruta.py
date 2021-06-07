from operator import itemgetter

get_peso = itemgetter(1)
get_valor = itemgetter(2)

def total_peso(paquetes):
    return sum(get_peso(x) for x in paquetes)

def total_valor(paquetes):
    return sum(get_valor(x) for x in paquetes)

def combinaciones(paquetes, peso_maximo):
    paquete = [ p for p in paquetes if get_peso(p) <= peso_maximo ]
    resultado = []
    for p in paquete:
        res = combinaciones([x for x in paquete if x!=p], peso_maximo - get_peso(p))
        if len(res) == 0:
            resultado.append([p])
        else:
            resultado.extend([[p]+x for x in res])
    return resultado

