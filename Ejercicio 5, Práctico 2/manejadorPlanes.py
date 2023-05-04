import csv
from ClasePlanAhorro import PlanAhorro as plan

class ManejadorPlan:
    __lista = []

    def __init__(self,lista = ''):
        self.__lista = []

    def __str__(self):
        s = ''
        for plan in self.__lista:
            s += str(plan) + '\n'
        return s

    def agregar(self,objeto):
        self.__lista.append(objeto)

    def testManejador(self):
        archi = open('Planes')
        reader = csv.reader(archi,delimiter=(';'))
        for i in reader:
            codigo = int(i[0])
            modelo = i[1]
            version = i[2]
            valor = float(i[3])
            objeto = plan(codigo,modelo,version,valor)
            self.agregar(objeto)
        archi.close()

    def obtenerInf(self,i):  #Inciso 1
        return self.__lista[i].getCodigo(),self.__lista[i].getModelo(),self.__lista[i].getVersion(),self.__lista[i].getValor()

    def actualizarValor(self,i,nv):  #Inciso 1
        self.__lista[i].actualizarValor(nv)

    def calculoValorCuota(self,valor):  #inciso 2
        print('\n Autos cuyas cuotas son menores a las ingresadas.')
        for plan in self.__lista:
            if(plan.valorCuota() < valor):
                print('\n Valor de la cuota: ${}'.format(plan.valorCuota()))
                print(plan)

    def calculo(self):  #iniciso 3
        for plan in self.__lista:
            print('\n Para el vehiculo {}, la licitacion es de ${}'.format(plan.getModelo(),plan.licitar()))