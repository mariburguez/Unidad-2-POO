class Viajero:
    __numViajero = int
    __dni = int
    __nombre = str
    __apellido = str
    __millasAcum = int
    
    
    def __init__ (self,numViajero,dni,nombre,apellido,millasAcum):
        self.__numViajero = numViajero
        self.__dni = dni
        self.__nombre = nombre
        self.__apellido = apellido
        self.__millasAcum = millasAcum
        
    
    def __str__ (self):
        return '%s    %s   %s     %s    %s' % (self.__numViajero,self.__dni,self.__nombre,self.__apellido,self.__millasAcum)
    
    def numeroViajero (self):
        return self.__numViajero
    
    def cantidadTotalMillas (self):
        return self.__millasAcum
    
    def nuevasMillas (self,millasNuevas):
        self.__millasAcum += millasNuevas
        
    def canjearMillas (self,canje):
        while (canje >= self.__millasAcum):
            print('\n Error, usted no posee esas millas para canjear. Usted dispone de {}.'.format(self.__millasAcum))
            canje = int(input('\n Vuelva a ingresar: '))
        print('\n CANJE EXITOSO.')
        self.__millasAcum = self.__millasAcum - canje
        print('\n Usted dispone de {} millas acumuladas.'.format(self.__millasAcum))