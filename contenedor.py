# coding: utf-8
import random
import sys
import time

import bottom_up as bottomUp
import fuerza_bruta as fuerzaBruta
import top_down_memorizacion as topDown

global pesoMaximo
global cantElementos
numIteraciones = 0
listaPesos = []
listasGanancias = []
listaTiempos = []


# Se encarga de leer el archivo y guardar los datos para mandarlos a procesar
def leerArchivo(nombreArchivo):
    f = open(nombreArchivo, 'r')

    primeraLinea = True
    global pesoMaximo, listaPesos, listasGanancias
    pesoMaximo = 0
    prueba = f.readlines()
    pesoMaximo = prueba[0]
    datos = []
    for linea in range(len(prueba)):
        lineaSeparada = prueba[linea].split('\n')
        datos.append(lineaSeparada[0].split(','))

    for i in range(len(datos)):
        if i == 0:
            pesoMaximo = int(datos[0][0])
        else:
            listaPesos.append(int(datos[i][0]))
            listasGanancias.append(int(datos[i][1]))
    f.close()
    return


# Función principal en donde se lee los argumentos que vienen de la lista de comandos.
# Si el paranetro entrante es -a manda a llamar la función archivo.
# Si el parametro entrante es -p manda a llamar la función aleatorio.
# Sino retorna
def main():
    numAlgoritmo = int(sys.argv[1])
    comando = sys.argv[2]
    if (comando == "-a"):
        archivo()
    elif (comando == "-p"):
        aleatorio()
    algoritmo(numAlgoritmo)
    return


# Se encarga de procesar la entrada cuando se recibe el parametro -p
# Crea un problema aleatorio
def aleatorio():
    global pesoMaximo, cantElementos, numIteraciones
    pesoMaximo = int(sys.argv[3])
    cantElementos = int(sys.argv[4])
    rangoPesos = sys.argv[5]
    rangoGanancias = sys.argv[6]
    numIteraciones = int(sys.argv[7])
    listRangosPeso = rangoPesos.split('-')
    listRangosGanancias = rangoGanancias.split('-')
    for i in range(0, cantElementos):
        listaPesos.append(random.randint(int(listRangosPeso[0]), int(listRangosPeso[1])))  # Mete cada uno de los pesos random a la lista de pesos
        listasGanancias.append(random.randint(int(listRangosGanancias[0]), int(listRangosGanancias[1])))  # Mete cada uno de las ganancias random a la lista de ganancias


# Se encarga de procesar la entrada cuando se recibe el parametro -a
# Se manda a llamar la función leer archivo
def archivo():
    global cantElementos, numIteraciones
    nombreArchivo = sys.argv[3]
    numIteraciones = int(sys.argv[4])
    leerArchivo(nombreArchivo)
    cantElementos = len(listasGanancias)


# Se encarga de llamar al algoritmo a utilizar según el numero de algoritmo que le entre en la línea de comando
# 1 -> Ejecuta la función Fuerza Bruta
# 2 -> Ejecuta la función Bottom-Up
# 3 -> Ejecuta la función Top-Down
def algoritmo(numAlgoritmo):
    global numIteraciones
    if numAlgoritmo == 1:
        while numIteraciones > 0:
            inicio = time.time()
            print("Fuerza Bruta", fuerzaBruta.fuerza_bruta(pesoMaximo, listaPesos, listasGanancias, cantElementos))
            fin = time.time()
            tiempo = fin - inicio  # Duración del algoritmo
            listaTiempos.append(tiempo)
            numIteraciones -= 1
        tiempoPromedio = round(sum(listaTiempos) / len(listaTiempos), 7)  # Tiempo promedio entre todos los tiempo de las ejecuciones del algoritmo
        print("Tiempo Promedio: ", tiempoPromedio)
    elif numAlgoritmo == 2:
        while numIteraciones > 0:
            inicio = time.time()
            print("Bottom-Up ", bottomUp.bottom_up(pesoMaximo, listaPesos, listasGanancias, cantElementos))
            fin = time.time()
            tiempo = fin - inicio  # Duración del algoritmo
            listaTiempos.append(tiempo)
            numIteraciones -= 1
        tiempoPromedio = round(sum(listaTiempos) / len(listaTiempos), 7)  # Tiempo promedio entre todos los tiempo de las ejecuciones del algoritmo
        print("Tiempo Promedio: ", tiempoPromedio)
    elif numAlgoritmo == 3:
        while numIteraciones > 0:
            inicio = time.time()
            print("Top-Down ", topDown.top_down(pesoMaximo, listaPesos, listasGanancias, cantElementos))
            fin = time.time()
            tiempo = fin - inicio  # Duración del algoritmo
            listaTiempos.append(tiempo)
            numIteraciones -= 1
        tiempoPromedio = round(sum(listaTiempos) / len(listaTiempos), 7)  # Tiempo promedio entre todos los tiempo de las ejecuciones del algoritmo
        print("Tiempo Promedio: ", tiempoPromedio)
    else:
        return


main()
