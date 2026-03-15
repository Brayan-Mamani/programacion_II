import math


def promedio(lista):
    return sum(lista) / len(lista)


def desviacion(lista):
    prom = promedio(lista)
    suma = 0
    
    for x in lista:
        suma += (x - prom) ** 2

    return math.sqrt(suma / (len(lista) - 1))



datos = list(map(float, input("Ingrese 10 numeros: ").split()))

print("El promedio es", promedio(datos))
print("La desviacion estandar es", desviacion(datos))

import math

class Estadistica:

    def __init__(self, datos):
        self.__datos = datos

    def __str__(self):
        return f"Datos: {self.__datos}"

    
    def promedio(self):
        return sum(self.__datos) / len(self.__datos)

    
    def desviacion(self):
        prom = self.promedio()
        suma = 0

        for x in self.__datos:
            suma += (x - prom) ** 2

        return math.sqrt(suma / (len(self.__datos) - 1))

    
    def getDatos(self):
        return self.__datos



class Main():

    datos = list(map(float, input("Ingrese 10 numeros: ").split()))

    estadistica = Estadistica(datos)

    print("El promedio es", estadistica.promedio())
    print("La desviacion estandar es", estadistica.desviacion())