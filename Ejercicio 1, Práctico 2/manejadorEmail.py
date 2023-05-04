import csv
from claseEmail import Email

class Manejador:
    __lista = []
    
    def __init__ (self,lista = ''):
        self.__lista = []
        
    def __str__(self):
        s = ''
        for Email in self.__lista:
            s += str(Email) + '\n'
        return s
            
            
        
    def agregarEmail (self,email):
        self.__lista.append(email)
        
    def testManejador (self):
        archi = open('ejercicio1')
        reader = csv.reader(archi,delimiter = ',')
        for i in reader:
            id = i[0]
            dom = i[1]
            tip = i[2]
            contra = 0
            email = Email(id,dom,tip,contra)
            self.agregarEmail(email)
        archi.close()
    
    def repetido (self,dom):
        cont = 0
        for Email in self.__lista:
            if (dom == Email.getDominio()):
                cont +=1
        return cont