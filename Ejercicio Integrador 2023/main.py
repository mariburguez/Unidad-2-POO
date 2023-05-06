from os import system
from manejadorCama import manejadorCama as maneCama
from manejadorMedicamento import manejadorMedicamento as maneMedi
from claseMedicamento import Medicamento as medi
from claseCama import Cama as cama

def menu():
    opcion = 0
    salir = False
    print('\n-----------MENU DE OPCIONES-----------')
    while not salir:
        print('\n1- Ver camas.')
        print('\n2- Ver medicamentos.')
        print('\n3- Paciente dado de alta.')
        print('\n4- Pacientes Internados.')
        print('\n5 - Salir')
        opcion = int(input('\nIngrese opcion: '))

        if(opcion == 1):
            print('idCama habitacion estado apellido nombre diagnostico fechaInternacion fechaAlta')
            print(objetoCama)
            system('pause')
        if(opcion == 2):
            print('\nidCama idMedicamento nombreComercial monodroga       presentacion  cantidadAplicada precioTotal')
            print(objetoMedicamento)
            system('pause')
        if(opcion == 3):
            nom = input('\nIngrese nombre del paciente: ')
            ape = input('\nIngrese apellido del paciente: ')
            NyA = nom + ape
            idCama = objetoCama.buscaPaciente(nom)  #Encuentra ID
            print(idCama)
            hab= objetoCama.obtener(idCama,1)
            diag = objetoCama.obtener(idCama,2)
            f = objetoCama.obtener(idCama,3)
            fa = objetoCama.obtener(idCama,4)
            print('\nPaciente: {}    Cama: {}   Habitacion: {}\nDiagnostico: {}  Fecha de Internacion: {}\nFecha de alta: {}'.format(NyA,idCama,hab,diag,f,fa))
            print('\nMedicamento      /Monodroga      Presentacion    Cantidad   Precio')
            total = objetoMedicamento.obtener(idCama)
            print('\nTotal adeudado:                                             ',total)
            system('pause')
        if(opcion == 4):
            diag = input('\nIngrese diagnostico: ')
            objetoCama.buscar(diag)
            system('pause')

        if(opcion == 5):
            salir = True


if __name__ == '__main__':
    objetoCama = maneCama(3)
    objetoCama.testManejador()
    objetoMedicamento = maneMedi()
    objetoMedicamento.testManejador()
    menu()
