from ViajeroFrecuente import Viajero as viaje
from manejadorViajero import manejador as mane

if __name__ == '__main__':
    objeto = mane()
    objeto.TestManejador()
    print('\n--------------------INCISO 1--------------------')

    viajero = objeto.mayor()
    print('\nViajero con mayor cantidad de millas acumuladas: \nCOD    DNI     NOMBRE   APELLIDO   MILLAS\n{}'.format(viajero))

    print('\n--------------------INCISO 2------------------')
    viajero = viajero + 100
    print('\nMillas acumuladas: {}'.format(viajero))

    print('\n--------------------INCISO 3-----------------')
    viajero = viajero - 100
    print('\nMillas acumuladas: {}'.format(viajero))