# coding: utf-8
import random
import sys
import time


import minaOroFuerzaBruta as minaOroFuerzaBruta
import minaOroDinamico as minaOroDinamico

global cantElementos
numIteraciones = 0
filas =0
columnas=0
matriz=[]
listaColumnas=[]
listaTiempos=[]


# Se encarga de leer el archivo y guardar los datos para mandarlos a procesar
def leerArchivo(nombreArchivo):
    f = open(nombreArchivo, 'r')
    global matriz,filas,columnas
    archivo = f.readlines()
    filas=len(archivo)
    for i in range(0,len(archivo)):
        lineaSeparada = []
        linea = archivo[i].split('\n')
        n=linea[0].split(',')
        for j in n :
            lineaSeparada.append(int(j))
        matriz.append(lineaSeparada)
    columnas=len(lineaSeparada)
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
    global numIteraciones,filas,columnas
    filas = int(sys.argv[3])
    columnas = int(sys.argv[4])
    minValorOro = int(sys.argv[5])
    maxValorOro = int(sys.argv[6])
    numIteraciones = int(sys.argv[7])

    for i in range(0, filas):
        listaColumnas=[]
        for j in range(0,columnas):
            listaColumnas.append(random.randint(minValorOro, maxValorOro))  # Mete cada uno de los costos random a la lista de columnas
        matriz.append(listaColumnas)


# Se encarga de procesar la entrada cuando se recibe el parametro -a
# Se manda a llamar la función leer archivo
def archivo():
    global numIteraciones
    nombreArchivo = sys.argv[3]
    numIteraciones = int(sys.argv[4])
    leerArchivo(nombreArchivo)


# Se encarga de llamar al algoritmo a utilizar según el numero de algoritmo que le entre en la línea de comando
# 1 -> Ejecuta la función Fuerza Bruta
# 2 -> Ejecuta la función Dinámica
def algoritmo(numAlgoritmo):
    global numIteraciones
    if numAlgoritmo == 1:
        print("****** Fuerza Bruta ******")
        while numIteraciones > 0:
            inicio = time.time()
            print("Oro máximo recolectado",minaOroFuerzaBruta.minaOroFuerzaBruta(matriz,columnas,filas))
            fin = time.time()
            tiempo = fin - inicio  # Duración del algoritmo
            listaTiempos.append(tiempo)
            numIteraciones -= 1
        tiempoPromedio = round(sum(listaTiempos) / len(listaTiempos), 7)  # Tiempo promedio entre todos los tiempo de las ejecuciones del algoritmo
        print("Tiempo Promedio: ", tiempoPromedio)
    elif numAlgoritmo == 2:
        print("****** Dinámico ******")
        while numIteraciones > 0:
            inicio = time.time()
            print("Oro máximo recolectado ",minaOroDinamico.minaOroDinamico(matriz,filas,columnas))
            fin = time.time()
            tiempo = fin - inicio  # Duración del algoritmo
            listaTiempos.append(tiempo)
            numIteraciones -= 1
        tiempoPromedio = round(sum(listaTiempos) / len(listaTiempos), 7)  # Tiempo promedio entre todos los tiempo de las ejecuciones del algoritmo
        print("Tiempo Promedio: ", tiempoPromedio)
    else:
        return


main()