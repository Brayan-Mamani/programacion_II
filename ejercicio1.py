import time
import random

class Cronometro:
    def __init__(self):

        self.__inicia = time.time()
        self.__finaliza = 0

    def __str__(self):
        return f"Cronometro -> Inicio: {self.__inicia}, Final: {self.__finaliza}"

    
    def iniciar(self):
        self.__inicia = time.time()

    
    def detener(self):
        self.__finaliza = time.time()

    
    def lapsoDeTiempo(self):
        return (self.__finaliza - self.__inicia) * 1000

    
    def getInicia(self):
        return self.__inicia

    def getFinaliza(self):
        return self.__finaliza


# Ordenacion por seleccion
def ordenacionSeleccion(lista):
    n = len(lista)

    for i in range(n):
        minimo = i
        for j in range(i+1, n):
            if lista[j] < lista[minimo]:
                minimo = j

        lista[i], lista[minimo] = lista[minimo], lista[i]


class Main():

    numeros = [random.randint(0,1000000) for i in range(100000)]
    cronometro = Cronometro()
    print("Iniciando ordenacion...")
    cronometro.iniciar()
    ordenacionSeleccion(numeros)
    cronometro.detener()
    print("Tiempo de ejecucion:", cronometro.lapsoDeTiempo(), "milisegundos")