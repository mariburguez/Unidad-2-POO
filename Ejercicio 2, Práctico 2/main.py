import os
from ViajeroFrecuente import Viajero as viaje
from manejadorViajero import manejador as mane

def menu(nro):
    Viaje = objeto.obtenerViajero(nro)
    salir = False
    opcion = 0
    while not salir:
        print('--------------------MENU DE OPCIONES------------------')
        print('1- CONSULTAR CANTIDAD DE MILLAS.')
        print('2- ACUMULAR MILLAS.')
        print('3- CANJEAR MILLAS.')
        print('4 - SALIR.')
        opcion = int(input('\n ingrese opcion: '))
        
        if(opcion == 1):
            print('\n La cantidad total de millas es de: {}'.format(Viaje.cantidadTotalMillas()))
        
        if(opcion == 2):
            millasNuevas = int(input('\n Ingrese cantidad de millas nuevas: '))
            Viaje.nuevasMillas(millasNuevas)
            print('\n La cantidad de millas es de {}'.format(Viaje.cantidadTotalMillas()))
        
        if(opcion == 3):
            canje = int(input('\n Ingrese cant de millas a canjear: '))
            Viaje.canjearMillas(canje)
            
        if(opcion == 4):
            salir = True

        
        

if __name__ == "__main__":
    objeto = mane()
    objeto.TestManejador()
    print('NUMERO    DNI     NOMBRE       APELLIDO   MILLAS')
    print(objeto)
    nro = int(input('\n Ingrese numero de viajero a consultar: '))
    condicion = objeto.verificar(nro)
    while(condicion != 1):
        condicion = print('\n El nro de viajero no existe. Vuelva a ingresar: ')
    
    menu(nro)