import numpy as np
import csv
from claseCama import Cama

class manejadorCama:
    __cantidad = 0
    __dimension = 0
    __incremento = 1

    def __init__(self,dimension,incremento = 1):
        self.__Cama = np.empty(dimension,dtype = Cama)
        self.__cantidad = 0
        self.__dimension = dimension

    def __str__(self):
        s = ''
        for Cama in self.__Cama:
            s += str(Cama) + '\n'
        return s

    def agregarCama (self,cama):
        if self.__cantidad == self.__dimension:
            self.__dimension += self.__incremento
            self.__Cama.resize(self.__dimension)
        self.__Cama[self.__cantidad] = cama
        self.__cantidad += 1

    def testManejador(self):
        archi = open('Camas')
        reader = csv.reader(archi,delimiter=';')
        for i in reader:
            id = i[0]
            hab = i[1]
            estado = i[2]
            nom = i[3]
            ape = i[4]
            diag = i[5]
            fInternacion = i[6]
            fAlta = i[7]
            objeto = Cama(id,hab,estado,nom,ape,diag,fInternacion,fAlta)
            self.agregarCama(objeto)
        archi.close()

    def buscaPaciente(self,nom):
        for Cama in self.__Cama:
            if(Cama.getApellido() == nom):
                return Cama.getId()

    def obtener(self,id,nro):
        for Cama in self.__Cama:
            if(Cama.getId() == id):
                if(nro == 1):
                    return Cama.getHabitacion()
                if(nro == 2):
                    return Cama.getDiagnostico()
                if(nro == 3):
                    return Cama.getFechaInternacion()
                else:
                    return Cama.getFechaAlta()

    def buscar(self,diag):
        for Cama in self.__Cama:
            if (Cama.getDiagnostico() == diag):
                print('\nCama: {}\nHabitacion: {}\nApellido:{}\nNombre: {}'.format(Cama.getId(),Cama.getHabitacion(),Cama.getNombre(),Cama.getApellido()))
                break;
