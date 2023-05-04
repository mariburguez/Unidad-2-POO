from claseConjunto import Conjunto as conjunto

class manejador:
    def __init__(self):
        self.__A = []
        self.__B = []

    def A(self,objeto):
        self.__A.append(objeto)

    def B(self,objeto):
        self.__B.append(objeto)

    def mostrarA(self):
        print('\n LISTA A: \n')
        s = ''
        for conjunto in self.__A:
            s += str(conjunto)
        return s

    def mostrarB(self):
        print('\n LISTA B: \n')
        c = ''
        for conjunto in self.__B:
            c += str(conjunto)
        return c

    def agregarA(self,nro):
        objeto = conjunto(nro)
        self.A(objeto)

    def agregarB(self,nro):
        objeto = conjunto(nro)
        self.B(objeto)

    def union(self):
        return max(self.__A)