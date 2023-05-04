class Registro:
    __temperatura = float
    __humedad = float
    __presión = float
    
    def __init__(self,temperatura,humedad,presión):
        self.__temperatura = temperatura
        self.__humedad = humedad
        self.__presión = presión
        
    def __str__(self):
        return '%s  %s  %s' % (self.__temperatura,self.__humedad,self.__presión)
    
    def getTemperatura(self):
        return self.__temperatura
    def getHumedad(self):
        return self.__humedad
    def getPresion(self):
        return self.__presión