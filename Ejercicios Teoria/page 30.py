class Punto:
    __x = 0
    __y = 0
    def inicializar(self,v1, v2):
        self.__x = v1
        self.__y = v2
    def setX(self, v):
        self.__x = v
    def getX(self):
        return self.__x
    def setY(self, v):
        self.__y = v
    def getY(self):
        return self.__y
    def mostrarDatos(self):
        print("(x,y) = (",self.__x,',', self.__y,")")
if __name__=='__main__':
    unPunto = Punto()
    otroPunto = Punto()
unPunto.inicializar(3,4)
otroPunto.inicializar(4,7)
unPunto.mostrarDatos()
otroPunto.mostrarDatos()