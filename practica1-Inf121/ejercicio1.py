import time
import random

class Cronometro:
    def __init__(self):
        # inicia con la hora actual
        self._inicia = time.time()
        self._finaliza = 0

    def __str__(self):
        return f"Cronometro -> Inicio: {self._inicia}, Final: {self._finaliza}"

    # a) metodo para reiniciar el cronometro
    def iniciar(self):
        self._inicia = time.time()

    # b) metodo para detener el cronometro
    def detener(self):
        self._finaliza = time.time()

    # c) metodo que retorna el tiempo en milisegundos
    def lapsoDeTiempo(self):
        return (self._finaliza - self._inicia) * 1000

    # Getters
    def getInicia(self):
        return self._inicia

    def getFinaliza(self):
        return self._finaliza


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

    # generar 100000 numeros aleatorios
    numeros = [random.randint(0,1000000) for i in range(100000)]

    cronometro = Cronometro()

    print("Iniciando ordenacion...")

    cronometro.iniciar()

    ordenacionSeleccion(numeros)

    cronometro.detener()

    print("Tiempo de ejecucion:", cronometro.lapsoDeTiempo(), "milisegundos")