import csv
from claseViajero import Viajero as viaje

class manejador:
    def __init__(self):
        self.__lista = []

    def __str__(self):
        s = ''
        for viaje in self.__lista:
            s += str(viaje) + '\n'
        return s

    def agregar(self,objeto):
        self.__lista.append(objeto)

    def testManejador(self):
        j = 0
        archi = open('viajero')
        reader = csv.reader(archi,delimiter = ',')
        for i in reader:
            num = j
            dni = i[0]
            nom = i[1]
            ape = i[2]
            millas = int(i[3])
            objeto = viaje(num,dni,nom,ape,millas)
            self.agregar(objeto)
            j = j+1
        archi.close()

    def mayor(self):
        return max(self.__lista)