class Ventana:
    __titulo = str
    __valorXVSI = int
    __valorYVSI = int
    __valorXVID = int
    __valorYVID = int


    def __init__ (self,titulo,valorXVSI = 0,valorYVSI = 0,valorXVID = 500,valorYVID = 500):
        if(valorXVSI >= 0 and valorYVSI >=0 and valorXVID <= 500 and valorYVID <= 500):
            self.__titulo = titulo
            self.__valorXVSI = valorXVSI
            self.__valorYVSI = valorYVSI
            self.__valorXVID = valorXVID
            self.__valorYVID = valorYVID
        else:
            print('\n Valores fuera de rango.')

    def mostrar (self):
        print ('\n VSI (X,Y): ({},{}) \n VSD (X,Y): ({},{})'.format(self.__valorXVSI,self.__valorYVSI,self.__valorXVID,self.__valorYVID))

    def getTitulo(self):
        return self.__titulo
    def alto(self):
        return (self.__valorXVSI - self.__valorXVID)
    def ancho(self):
        return (self.__valorYVSI - self.__valorYVID)

    def moverDerecha(self,nro=1):
        self.__valorXVSI = self.__valorXVSI + nro
        self.__valorXVID = self.__valorXVID + nro

    def moverIzquierda(self,nro=1):
        self.__valorXVID = self.__valorXVID - nro
        self.__valorXVSI = self.__valorXVSI - nro

    def bajar(self,nro=1):
        self.__valorYVSI = self.__valorYVSI - nro
        self.__valorYVID = self.__valorYVID - nro

    def subir(self,nro=1):
        self.__valorYVID = self.__valorYVID + nro
        self.__valorYVSI = self.__valorYVSI + nro
