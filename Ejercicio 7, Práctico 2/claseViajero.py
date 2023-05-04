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
        return (self.__millasAcum >= 100)

    def __eq__(self, other):
        return (self.__millasAcum == 100)

    def __add__(self, other):
        return (self.__millasAcum + other)

    def __radd__(self, other):
        return (self.__millasAcum + other)

    def __sub__(self, other):
        return (self.__millasAcum - other)

    def __rsub__(self, other):
        return (self.__millasAcum - other)