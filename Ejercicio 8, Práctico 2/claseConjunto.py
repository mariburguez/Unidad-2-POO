class Conjunto:
    def __init__(self):
        self.__listaA = set()  #Tengo que definirla asi sino no me hace la resta

    def __str__(self):
        s = ''
        for i in self.__listaA:
            s += str(i) + ' '
        return s


    def agregar(self,nros):
        for i in nros:
            self.__listaA.add(i)

    def __add__(self,other):
        C = Conjunto()
        C.agregar(self.__listaA | other.__listaA)
        return C

    def __sub__(self,other):
        C = Conjunto()
        C.agregar(self.__listaA - other.__listaA)
        return C

    def __eq__(self, other):
        return self.__listaA == other.__listaA