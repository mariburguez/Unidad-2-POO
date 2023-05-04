from manejadorViajero import manejador as mane


if __name__ == '__main__':
    objeto = mane()
    objeto.testManejador()
    print('\nCOD    DNI     NOMBRE  APELLIDO     MILLAS')
    print(objeto)
    v = objeto.mayor()
    print('\n---------------INCISO 1------------')
    print('Viajero con 100 millas: \n {}'.format(v)) if v == 100 else print('\n No hay viajeros con 100 millas.')
    v = 100 + v
    print('\n---------------INCISO 2-----------\nAcumular millas por derecha\n {}'.format(v))
    v = 100 - v
    print('\n---------------INCISO 3------------\nCanjear millas por derecha\n {}'.format(v))