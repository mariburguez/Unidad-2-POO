class PlanAhorro:
    cantCuotas = 60
    cantCuotasPagas = 10

    def __init__(self,codigo,modelo,version,valor):
        self.__codigo = codigo
        self.__modelo = modelo
        self.__version = version
        self.__valor = valor

    def __str__(self):
        return '%s    %s    %s   %s' % (self.__codigo,self.__modelo,self.__version,self.__valor)

    @classmethod
    def getCantCuotasPagas(cls):
        return cls.cantCuotasPagas

    def getCodigo(self):
        return self.__codigo
    def getModelo(self):
        return self.__modelo
    def getVersion(self):
        return self.__version
    def getValor(self):
        return self.__valor

    def valorCuota(self):
        return round(float(self.__valor + self.__valor * 0.10) / PlanAhorro.cantCuotas,2)

    def actualizarValor(self,valor):
        self.__valor = valor

    def licitar(self):
        return round(float(self.valorCuota() + PlanAhorro.cantCuotasPagas),2)

    def modificar(self,c):
        PlanAhorro.cantCuotasPagas = c