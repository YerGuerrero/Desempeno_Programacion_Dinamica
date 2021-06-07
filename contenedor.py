import sys
import fuerza_bruta as fuerzaBruta
from pprint import pprint

#Paquetes: "Nombre del paquete", Kilos, Precio
PAQUETES = (
    ("Paquete 1", 9, 150), ("Paquete 2", 9, 160), ("Paquete 3", 153, 200), ("Paquete 4", 50, 160),
    ("Paquete 5", 15, 60), ("Paquete 6", 66, 45), ("Paquete 7", 27, 60), ("Paquete 8", 39, 40),
    ("Paquete 9", 230, 591), ("Paquete 10", 520, 10), ("Paquete 11", 110, 70), ("Paquete 12", 32, 30))

#carga máxima del camión
PESOMAXIMO = 150

def leerArchivo(nombreArchivo):
    f = open(nombreArchivo, 'r')
    mensaje = f.read()
    print(mensaje)
    f.close()
    return

def main():
    numAlgoritmo= sys.argv[0]
    comando= sys.argv[1]
    print(comando)
    if (comando== "-a"):
        nombreArchivo= sys.argv[2]
        numIteraciones= sys.argv[3]
        leerArchivo(nombreArchivo)
    elif (comando == "-p"):
        print("Ejemplo aleatorio")
    # solución
    sol = max(fuerzaBruta.combinaciones(PAQUETES, PESOMAXIMO), key=fuerzaBruta.total_valor)
    print("Peso {} Valor {}".format(fuerzaBruta.total_peso(sol), fuerzaBruta.total_valor(sol)))
    pprint(sol)
    return



main()