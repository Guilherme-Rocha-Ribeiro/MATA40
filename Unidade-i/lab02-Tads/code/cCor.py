# #########################################
# Define um Tipo Abstrato de Dados (TAD) 
# para armazenar cores no formato RGB
# #########################################

class cCor:

    def __init__(self, r=1.0, g=1.0, b=1.0):
        self.r = r
        self.g = g
        self.b = b

    def setCor(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b

    def setR(self, r):
        if (r >= 0.0) and r <= 1.0:
            self.r = r

    def setG(self, g):
        if (g >= 0.0) and g <= 1.0:
            self.g = g

    def setB(self, b):
        if (b >= 0.0) and b <= 1.0:
            self.b = b

    def getCor(self):
        return self.r, self.g, self.b

    def getR(self):
        return self.r

    def getG(self):
        return self.g

    def getB(self):
        return self.b

    def __str__(self):
        return f'[ \u001b[31m{self.r},\t\u001b[32m{self.g},\t\u001b[34m{self.b} \u001b[37m ]'

    def __add__(self, c):

        if isinstance(c, cCor):
            r = self.r + c.r
            g = self.g + c.g
            b = self.b + c.b

        return self.__class__(r, g, b)

    def __mul__(self, factor):
        if (isinstance(factor, int) or isinstance(factor, float)) and (factor >=0.0) and (factor <= 1.0):
            r = self.r * factor
            g = self.g * factor
            b = self.b * factor

        elif isinstance(factor, cCor):
            r = self.r * factor.r
            g = self.g * factor.g
            b = self.b * factor.b

        return self.__class__(r, g, b)

# *******************************************************
# ***                                                 ***
# *******************************************************
if __name__ == '__main__':

    corPadrao   = cCor()
    naoCor      = cCor(-1.0, -1.0, -1.0)
    vermelho    = cCor( 1.0,  0.0, 0.0 )
    azul        = cCor( 0.0,  1.0, 0.0 )
    verde       = cCor( 0.0,  0.0, 1.0 )
    magenta     = vermelho + azul
    ciano       = azul + verde
    amarelo     = verde + vermelho

    print(f'Cor Padrao = {str(corPadrao)}')
    print(f'Nao Cor = {str(naoCor)}')

    print(f'Cores basicas: ', end='')
    print(str(vermelho), str(verde), str(azul))
    print(f'Cores complementares: ', end='')
    print(str(magenta), str(ciano), str(amarelo))
