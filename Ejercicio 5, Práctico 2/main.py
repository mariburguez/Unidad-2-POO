import os
from ClasePlanAhorro import PlanAhorro as plan
from manejadorPlanes import ManejadorPlan as mane

def menu():
    opcion = 0
    salir = False
    while not salir:
        print('\n---------------------MENU DE OPCIONES--------------------')
        print('\n 1- Actualizar el valor del vehículo.')
        print('\n 2- Dado un valor, mostrar código del plan, modelo y versión del vehículo cuyo valor de la cuota sea inferior al valor dado.')
        print('\n 3- Mostrar el monto que se debe haber pagado para licitar el vehículo (cantidad de cuotas para licitar * importe de la cuota).')
        print('\n 4- Dado el código de un plan, modificar la cantidad cuotas que debe tener pagas para licitar.')
        print('\n 5- Salir.')
        opcion = int(input('\n Ingrese opcion: '))

        if(opcion == 1):
            for i in range(5):
                print('\nCOD MODELO   VERSION       VALOR ')
                j = objeto.obtenerInf(i)
                print(j[0],  j[1],  j[2],   j[3])
                nuevoValor = input('\n Ingrese nuevo valor: ')  #Valor nuevo del vehiculo
                objeto.actualizarValor(i,nuevoValor)
                print('\nCOD MODELO   VERSION       VALOR ')
                j = objeto.obtenerInf(i)
                print(j[0], j[1], j[2], j[3])
                os.system('pause')

        if(opcion == 2):
            imp = float(input('\n Ingrese un valor: '))
            objeto.calculoValorCuota(imp)
            os.system('pause')

        if(opcion == 3):
            objeto.calculo()
            os.system('pause')

        if(opcion == 4):
            c = input('\n Ingrese cantidad de cuotas nuvas para licitar: ')
            plan.cantCuotasPagas = c
            print('\n Las cuotas para licitar un vehículo son {}.'.format(plan.getCantCuotasPagas()))
            os.system('pause')

        if(opcion == 5):
            salir = True


if __name__ == "__main__":
    objeto = mane()
    objeto.testManejador()
    menu()