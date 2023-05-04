import csv
from ViajeroFrecuente import Viajero as viaje

class manejador:
    __lista = []
    
    def __init__ (self,lista = ''):
        self.__lista = []
    
    def __str__ (self):
        s = ''
        for viaje in self.__lista:
            s += str(viaje) + '\n'
        return s
        
    def agregar (self,objeto):
        self.__lista.append(objeto)
        
    
    def TestManejador (self):
        archi = open('viajeros')
        j = 1
        reader = csv.reader(archi,delimiter = ',')
        for i in reader:
            num = j
            dni = i[0]
            nombre = i[1]
            apellido = i[2]
            millas = int(i[3])
            objeto = viaje(num,dni,nombre,apellido,millas)
            self.agregar(objeto)
            j = j+1
        archi.close()
        
    def verificar (self,nro):
        for viaje in self.__lista:
            if(nro == viaje.numeroViajero()):
                return 1
    
    def obtenerViajero (self,nro):
        return self.__lista[nro-1]