# #########################################
# Define um Tipo Abstrato de Dados (TAD) 
# para armazenar pontos em 2D com cor
# #########################################

import cCor

class cPontoCor:

    def __init__(self, x=0.0, y=0.0, c=cCor.cCor()):
        self.x = x
        self.y = y
        if isinstance(c, cCor.cCor):
            self.cor = c
        else:
            self.cor = cCor.cCor()

    def setX(self, x):
        self.x = x

    def setY(self, y):
        self.y = y

    def setCor(self, c):
        if isinstance(c, cCor.cCor):
            self.cor = c
        else:
            self.cor = cCor.cCor()

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def getCorPto(self):
        return self.cor

    def print(self):
        print("Pto =  ")
        print(f'( {self.x} , {self.y} ) {str(self.cor)}')

    def __str__(self):
        return f'( {self.x} , {self.y } ) {str(self.cor)}'

    def __add__(self, pto):
        if isinstance(pto, cPontoCor):
            x = self.x + pto.getX()
            y = self.y + pto.getY()
            c = self.cor + pto.getCorPto()

        return self.__class__(x, y, c)

# *******************************************************
# ***                                                 ***
# *******************************************************
if __name__ == '__main__':

    pBase       = cPontoCor()
    ptoVermelho = cPontoCor( 0.5,  0.5, cCor.cCor(1.0, 0.0, 0.0) )
    ptoAzul     = cPontoCor( 0.0,  0.5, cCor.cCor(0.0, 1.0, 0.0) )
    ptoVerde    = cPontoCor( 0.5,  0.0, cCor.cCor(0.0, 0.0, 1.0) )

    ptoMagenta  = ptoVermelho + ptoAzul
    ptoCiano    = ptoAzul + ptoVerde
    ptoAmarelo  = ptoVermelho + ptoVerde

    pBase.print()

    print(f'Os pontos gerados foram: ', end='')
    print(str(ptoVermelho), str(ptoAzul), str(ptoVerde))

    print(f'Os pontos compostos foram: ', end='')
    print(str(ptoMagenta), str(ptoCiano), str(ptoAmarelo))
