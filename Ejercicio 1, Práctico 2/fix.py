print("Practico 2 - Ejercicio 1")

class email:
    #ATRIBITOS DE LA CLASS"
    idCuenta= ""
    dominio= "nada"
    tipoDominio= "nada"
    contraseña="nada"
    
    #metodo constructor
    def _init_(self, idCuenta, dominio, tipoDominio, contraseña):
        self.idCuenta= idCuenta
        self.dominio=dominio 
        self.tipoDominio=tipoDominio
        self.contraseña=contraseña

    #Método “retornaEmail()” 
    def retornaEmail(self, idCuenta, dominio, tipoDominio):
        self.idCuenta= idCuenta
        self.dominio=dominio
        self.tipoDominio=tipoDominio
        nuevoEmail= idCuenta+"@"+dominio+"."+tipoDominio
        return nuevoEmail
    #retorna dominio: 
    def getDominio():
        return self.dominio
    
    #crear cuenta
    def crearCuenta(self):
        self.idCuenta=input("Dime tu idCuenta: ")
        self.dominio=input("Dime tu dominio: ")
        self.tipoDominio=input("Dime tu tipoDominio: ")
        self.tipoDominio=input("Dime tu contraseña: ")

if __name__=='__main__':
    #no se como instanciar (diapo 34)
    email1=email()
    #ingresa por tecado los datos
    idCuenta=input("Dime tu idCuenta: ")
    dominio=input("Dime tu dominio: ")
    tipoDominio=input("Dime tu tipoDominio: ")
#llamadas:
nuevo=email1.retornaEmail(idCuenta, dominio, tipoDominio)
print("correo", nuevo)

