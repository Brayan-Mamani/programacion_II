import math

class EcuacionCuadratica:

    def __init__(self, a, b, c):
        self.__a = a
        self.__b = b
        self.__c = c

    def __str__(self):
        return f"{self.__a}x^2 + {self.__b}x + {self.__c} = 0"


    def getDiscriminante(self):
        return (self.__b ** 2) - (4 * self.__a * self.__c)

   
    def getRaiz1(self):
        disc = self.getDiscriminante()
        if disc >= 0:
            return (-self.__b + math.sqrt(disc)) / (2 * self.__a)
        else:
            return 0

    
    def getRaiz2(self):
        disc = self.getDiscriminante()
        if disc >= 0:
            return (-self.__b - math.sqrt(disc)) / (2 * self.__a)
        else:
            return 0

    
    def getA(self):
        return self.__a

    def getB(self):
        return self.__b

    def getC(self):
        return self.__c

class Main():

    datos = input("Ingrese a, b, c: ").split()

    a = float(datos[0])
    b = float(datos[1])
    c = float(datos[2])

    ecuacion = EcuacionCuadratica(a, b, c)

    discriminante = ecuacion.getDiscriminante()

    if discriminante > 0:
        print("La ecuación tiene dos raíces", ecuacion.getRaiz1(), "y", ecuacion.getRaiz2())

    elif discriminante == 0:
        print("La ecuación tiene una raíz", ecuacion.getRaiz1())

    else:
        print("La ecuación no tiene raíces reales")