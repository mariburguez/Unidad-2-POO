from claseEmail import Email 
from manejadorEmail import Manejador as mane


if __name__ == '__main__':
    for i in range(1):
        nombre = input('Ingrese su nombre: ')
        idCuenta = input('Ingrese su id de cuenta: ')
        dominio = input('Ingrese su dominio (com): ')
        tipo = input('Ingrese su tipo de dominio: ')
        contra = input('Ingrese contraseña: ')
        email = Email(idCuenta,dominio,tipo,contra)
        
    #------------------------------INCISO 1--------------
    print('\n Estimado {}, te enviaremos tus mensajes a la dirección {}'.format(nombre, email.retornaEmail()))
    email.getDominio()
    
    #------------------------------INCISO 2---------------
    print('\n------------------CAMBIO DE CONTRASEÑA------------------')
    opcion = str(input('\n Desea cambiar la contraseña? (si/no): '))
    if (opcion == 'si'):
        email.cambiarContra()
        
    #-------------------------------INCISO 3--------------
    print('\n--------------------VALIDAR EMAIL----------------------')
    mail= input('\n Ingrese email para validarlo: ')
    nuevo = email.validar(mail)
    objeto = mane()
    objeto.agregarEmail(nuevo)
    objeto.testManejador()
    print('\n-----------------EMAILS-----------------')
    print (objeto)
    
    #-------------------------------INCISO 4--------------
    dom= input('\n Ingrese un dominio para ver si esta repetido: ')
    cont = objeto.repetido(dom)
    print('\n Hay {} emails con el dominio .{}.'.format(cont,dom))