from os import system
from claseRegistro import Registro as reg
from manejadorRegistro import Manejador as mane


def menu():
    salir = False
    opcion = 0
    while not salir:
        print('\n----------------------MENU DE OPCIONES--------------------')
        print('\n 1- Mostrar para cada variable día y hora de mayor y menor valor.')
        print('\n 2- Indicar la temperatura promedio de cada dia.')
        print('\n 3- Mostrar los datos de las variables por hora para un dia dado.')
        print('\n 4- Salir.')
        opcion = int(input('\n Ingrese opcion: '))
        
        if(opcion == 1):
            variables = ['temperatura', 'humedad', 'presion']
            for i in range(len(variables)):
                menorDia = objeto.menor(variables[i])
                mayorDia = objeto.mayor(variables[i])
                print('\n Dia y hora con menor valor.')
                print('\nVariable: {} \nDia: {} \nHora: {}'.format(variables[i],menorDia[0],menorDia[1]))
                system('pause')
                print('\n Dia y hora con mayor valor.')
                print('\nVariable: {} \nDia: {} \nHora: {}'.format(variables[i],mayorDia[0],mayorDia[1]))
                system('pause')

        if(opcion == 2):
            dia = 0
            for i in range(30):
                dia = dia + 1
                promedio = objeto.promedio(i)
                print('\n La temperatura promedio del dia {} fue de {}'.format(dia,promedio))
                system('pause')

        if(opcion == 3):
            dia = int(input('\n Ingrese un dia: '))
            dia = dia - 1
            print('\n DIA   TEMPERATURA   HUMEDAD   PRESIÓN')
            mostrar = objeto.mostrarPorDia(dia)
            system('pause')

        if(opcion == 4):
            salir = True
                
                
if __name__ == '__main__':
    objeto = mane()
    objeto.testManejador()
    menu()