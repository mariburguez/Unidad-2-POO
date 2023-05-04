import re

class Email:
    __idCuenta: str
    __tipoDominio: str
    __dominio:str
    __contraseña: str
    
    
    def __init__(self,idCuenta,tipoDominio,dominio,contraseña):
        self.__idCuenta = idCuenta
        self.__tipoDominio = tipoDominio
        self.__dominio = dominio
        self.__contraseña = contraseña
        
    def __str__(self):
        return '%s@%s.%s' % (self.__idCuenta,self.__tipoDominio,self.__dominio)
        
    def retornaEmail(self):
        return ('{}@{}.{}'.format(self.__idCuenta,self.__tipoDominio,self.__dominio))
        
    def getDominio (self):
        return self.__dominio
    
    def cambiarContra(self):
        contraVieja = input('Ingrese contraseña actual: ')
        while(contraVieja != self.__contraseña):
            contraVieja = input('Error, contraseña incorrecta. Vuelva a ingresar: ')
            
        contraNueva = input('Ingrese contraseña nueva: ')
        self.__contraseña = contraNueva
        print('Cambio de contraseña exitoso.')
    
    def validar(self,mail):
        if re.match ('^[(a-z0-9\_\-\.)]+@[(a-z0-9\_\-\.)]+\.[(a-z)]{2,15}$',mail):
            print('\n Correo ingresado correctamente.')
            em,em1 = mail.split('@')
            em1,em2 = em1.split('.')
            nuevacontra = input('Ingrese contraseña: ')
            nuevoMail = Email(em,em1,em2,nuevacontra)
            return nuevoMail
        else: print('\n Correo ingresado incorrecto.')
