import csv
from claseRegistro import Registro as reg


class Manejador:
    __lista = []
    
    def __init__(self):
        self.__lista = [[] for x in range(30)]
        
    def __str__ (self):
        s = ''
        for reg in self.__lista:
            s += str(reg) + '\n'
        return s
    
    def agregarLista (self,dia,objeto):
        self.__lista[dia-1].append(objeto)
    
    
    def testManejador (self):
        archi = open('Registros')
        reader = csv.reader(archi,delimiter = (','))
        for i in reader:
            dia = int(i[0])
            temperatura = float(i[2])
            humedad = float(i[3])
            presion = float(i[4])
            objeto = reg(temperatura,humedad,presion)
            self.agregarLista(dia,objeto)
        archi.close()
        
    def menor (self,variable):
        mini,dia,hora, valor= 999.9,0,0,0.0
        for i in range(len(self.__lista)):
            for j in range(len(self.__lista[i])):
                if(variable == 'temperatura'):
                    valor = self.__lista[i][j].getTemperatura()
                    
                elif(variable == 'humedad'):
                    valor = self.__lista[i][j].getHumedad()
                
                else:
                    valor = self.__lista[i][j].getPresion()
                
                if(mini > valor):
                    mini = valor
                    dia = i+1
                    hora = j+1
        return dia,hora
                
                
    
    def mayor (self,variable):
        maxi,dia,hora,valor = 0.0,0,0,0.0
        for i in range(len(self.__lista)):
            for j in range(len(self.__lista[i])):
                if(variable == 'temperatura'):
                    valor = self.__lista[i][j].getTemperatura()
                    
                elif(variable == 'humedad'):
                    valor = self.__lista[i][j].getHumedad()
                
                else: 
                    valor = self.__lista[i][j].getPresion()
                
                if(maxi < valor):
                    maxi = valor
                    dia = i+1
                    hora = j+1
        return dia,hora

    def promedio(self,hora):
        acum = 0.0
        for i in range(len(self.__lista)):
            for j in range(len(self.__lista[i])):
                acum = acum + self.__lista[hora][j].getTemperatura()
            acum = acum/24
            return round(acum,2)

    def mostrarPorDia (self,dia):
            i = dia + 1
            for j in range(len(self.__lista[dia])):
                print(i,    self.__lista[dia][j].getTemperatura(),    self.__lista[dia][j].getHumedad(),    self.__lista[dia][j].getPresion())