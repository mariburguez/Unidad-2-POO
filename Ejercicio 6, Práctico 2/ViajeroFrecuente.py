class Viajero:
    def __init__(self, numViajero, dni, nombre, apellido, millasAcum):
        self.__numViajero = numViajero
        self.__dni = dni
        self.__nombre = nombre
        self.__apellido = apellido
        self.__millasAcum = millasAcum

    def __str__(self):
        return '%s %s  %s  %s     %s' % (self.__numViajero, self.__dni, self.__nombre, self.__apellido, self.__millasAcum)

    def __gt__(self, other):
        return (self.__millasAcum > other.__millasAcum)
    def __add__(self, other):
        return (self.__millasAcum + 100)
    def __sub__(self,other):
        return (self.__millasAcum - 100)
