# #########################################
# Define um Tipo Abstrato de Dados (TAD) 
# para armazenar pontos em 2D
# #########################################

class cPonto:

    def __init__(self, x=0.0, y=0.0):
        self.x = x
        self.y = y

    def print(self):
        print(f'Pto =  ( {self.x} , {self.y} )')

    def setX(self, v):
        self.x = v

    def setY(self, v):
        self.y = v

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def __str__(self):
        return f'( {self.x} , {self.y } )'

    def __add__(self, pto):

        if isinstance(pto, cPonto):
            x = self.x + pto.x
            y = self.y + pto.y

        return self.__class__(x, y)

# *******************************************************
# ***                                                 ***
# *******************************************************
if __name__ == '__main__':

    p0 = cPonto()
    p1 = cPonto(-1.0, -1.0)
    p2 = cPonto( 1.0,  1.0)
    p3 = p1 + p2

    p0.print()
    p1.print()
    p2.print()
    p3.print()

    print(f'Os pontos gerados foram: ', end='')
    print(str(p1), str(p2), str(p3))
    print(f'P0 => ( {p0.getX()} , {p0.getY()} )')
