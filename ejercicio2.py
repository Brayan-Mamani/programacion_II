class EcuacionLineal:

    def __init__(self, a, b, c, d, e, f):
        self._a = a
        self._b = b
        self._c = c
        self._d = d
        self._e = e
        self._f = f

    def __str__(self):
        return f"{self._a}x + {self._b}y = {self._e} | {self._c}x + {self._d}y = {self._f}"

    # c) metodo que verifica si tiene solucion
    def tieneSolucion(self):
        return (self._a * self._d - self._b * self._c) != 0

    # d) metodo para obtener X
    def getX(self):
        return (self._e * self._d - self._b * self._f) / (self._a * self._d - self._b * self._c)

    # d) metodo para obtener Y
    def getY(self):
        return (self._a * self._f - self._e * self._c) / (self._a * self._d - self._b * self._c)

    
    def getA(self):
        return self._a

    def getB(self):
        return self._b

    def getC(self):
        return self._c

    def getD(self):
        return self._d

    def getE(self):
        return self._e

    def getF(self):
        return self._f
    
class Main():

    datos = input("Ingrese a, b, c, d, e, f: ").split()

    a = float(datos[0])
    b = float(datos[1])
    c = float(datos[2])
    d = float(datos[3])
    e = float(datos[4])
    f = float(datos[5])

    ecuacion = EcuacionLineal(a, b, c, d, e, f)

    if ecuacion.tieneSolucion():
        print("x =", ecuacion.getX(), ", y =", ecuacion.getY())
    else:
        print("La ecuación no tiene solución")