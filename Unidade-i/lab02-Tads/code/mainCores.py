# #########################################
# Programa que utiliza a Classe cCor
# #########################################

import cCor
import random

if __name__ == '__main__':

    cores = []

    for i in range(10):
        cores.append(cCor.cCor())

    for i in range(10):
        cores.append(cCor.cCor( random.randint(0, 100)/100, 
                                random.randint(0, 100)/100, 
                                random.randint(0, 100)/100) )

    for i in range(5):
        cores[i*2] = cores[i*2] * cores[10+i*2]

    for i in range(len(cores)):
        print(str(cores[i]))
