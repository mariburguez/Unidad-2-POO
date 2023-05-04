from os import system
from claseConjunto import Conjunto as conjunto

def menu():
    opcion = 0
    salir = False
    while not salir:
        print('\n-------------MENU DE OPCIONES------------------')
        print('\n1- Union de dos listas.')
        print('\n2- Intersección entre dos listas.')
        print('\n3- Verificar si son iguales las listas.')
        print('\n4- Salir.')
        opcion = int(input('\nIngrese opcion: '))

        while not salir:
            if(opcion == 1):
                print('\nUNION:',A+B)
                system('pause')

            if(opcion == 2):
                print('\nINTERSECCIÓN: ',A-B)
                system('pause')

            if(opcion == 3):
                print('\nNo son iguales') if((A == B) == False) else print('\n Son iguales.')
                system('pause')

            if(opcion == 4):
                salir = True


if __name__ == '__main__':
    A = conjunto()    #Tengo que declararlas como clase conjunto para poder realizar la resta.
    B = conjunto()
    A.agregar([1,2,3,4])
    B.agregar([3,4,1,2])
    print('\nLISTA A: ',A)
    print('\nLISTA B: ',B)
    system('pause')
    menu()