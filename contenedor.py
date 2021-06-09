#coding: utf-8
import sys
import fuerza_bruta as fuerzaBruta
import top_down_memorizacion as topDown
import bottom_up as bottomUp
import random
import time




global pesoMaximo
global cantElementos
numIteraciones=0
listaPesos=[]
listasGanancias=[]
listaTiempos=[]


def leerArchivo(nombreArchivo):
    f = open(nombreArchivo, 'r')
    primeraLinea=True
    global pesoMaximo,listaPesos,listasGanancias
    pesoMaximo=0
    prueba= f.readlines()
    pesoMaximo=prueba[0]
    datos=[]
    for linea in range (len(prueba)):
        lineaSeparada= prueba[linea].split('\n')
        datos.append(lineaSeparada[0].split(','))

    for i in range(len(datos)):
        if i==0:
            pesoMaximo= int(datos[0][0])
        else:
            listaPesos.append(int(datos[i][0]))
            listasGanancias.append(int(datos[i][1]))
    f.close()
    return

def main():
    numAlgoritmo= int(sys.argv[1])
    comando= sys.argv[2]
    if (comando== "-a"):
        archivo()
    elif (comando == "-p"):
        aleatorio()
    algoritmo(numAlgoritmo)
    return

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
        listaPesos.append(random.randint(int(listRangosPeso[0]), int(listRangosPeso[1])))
        listasGanancias.append(random.randint(int(listRangosGanancias[0]), int(listRangosGanancias[1])))

def archivo():
    global cantElementos, numIteraciones
    nombreArchivo = sys.argv[3]
    numIteraciones = int(sys.argv[4])
    leerArchivo(nombreArchivo)
    cantElementos = len(listasGanancias)

def algoritmo(numAlgoritmo):
    global numIteraciones
    if numAlgoritmo == 1:
        while numIteraciones>0:
            inicio = time.time()
            print("Fuerza Bruta",fuerzaBruta.fuerza_bruta(pesoMaximo,listaPesos,listasGanancias,cantElementos))
            fin = time.time()
            tiempo=fin-inicio
            listaTiempos.append(tiempo)
            numIteraciones-=1
        tiempoPromedio=round(sum(listaTiempos)/len(listaTiempos),7)
        print("Tiempo Promedio: ",tiempoPromedio)
    elif numAlgoritmo == 2:
        while numIteraciones>0:
            inicio = time.time()
            print("Bottom-Up ", bottomUp.bottom_up(pesoMaximo, listaPesos, listasGanancias, cantElementos))
            fin = time.time()
            tiempo=fin-inicio
            listaTiempos.append(tiempo)
            numIteraciones-=1
        tiempoPromedio=round(sum(listaTiempos)/len(listaTiempos),7)
        print("Tiempo Promedio: ",tiempoPromedio)
    elif numAlgoritmo == 3:
        while numIteraciones>0:
            inicio = time.time()
            print("Top-Down ", topDown.top_down(pesoMaximo, listaPesos, listasGanancias, cantElementos))
            fin = time.time()
            tiempo=fin-inicio
            listaTiempos.append(tiempo)
            numIteraciones-=1
        tiempoPromedio=round(sum(listaTiempos)/len(listaTiempos),7)
        print("Tiempo Promedio: ",tiempoPromedio)
    else:
        return

main()