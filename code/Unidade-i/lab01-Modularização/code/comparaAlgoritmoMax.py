# #################################
# Analisa numero de comparações dos
# algoritmos de minimo e máxixmo
# de um vetor de inteiros
# #################################

import sys
import random
from datetime import datetime

import minMaxVetor
import minMaxVetorII
import minMaxVetorIII

# *******************************************************
# *******************************************************

def imprimeVetor(vet, vPosMax=-1, vPosMin=-1):

    n = len(vet)

    impMax = vPosMax != -1
    impMin = vPosMin != -1

    print(f"[ ", end = '')
    for i in range(n-1):

        if impMax and i == vPosMax:
            print(f"\033[1;92m", end = '')
        elif impMin and i == vPosMin:
            print(f"\033[1;31m", end = '')
        else:
            print(f"\033[1;37m", end = '')

        print(f"{vet[i]}\033[1;37m, ", end = '') 

    if (impMax and n-1 == vPosMax):
        print(f"\033[1;92m", end = '')
    elif impMin and n-1 == vPosMin:
        print(f"\033[1;31m", end = '')
    else:
        print(f"\033[1;37m", end = '')

    print(f"{vet[n-1]}\033[1;37m]") 

    if impMax:
        print(f"Maior elemento da sequencia = {v[vPosMax]}")
    if impMin:
        print(f"Menor elemento da sequencia = {v[vPosMin]}")
    print(f"Quantidade de comparações = {qnt_cmpout}")
    print(end = "\n")


# *******************************************************
# ***                                                 ***
# *******************************************************
if __name__ == '__main__':

    v = []

    random.seed(int(datetime.now().strftime('%H%M%S')))

    if (len(sys.argv) > 1):
        n = int(sys.argv[1])
    else:
        n = 20

    if (len(sys.argv) > 2):
        ordem = str(sys.argv[2])
        if (ordem != 'rand' and ordem != 'decr' and ordem != 'cresc' ):
            print ("critério de geração: rand / decr / cresc")
            sys.exit()
    else:
        ordem = 'rand'

    for i in range(n):
        if (ordem == 'rand'):
            v.append(random.randint(0, 1000))
        elif (ordem == 'decr'):
            v.append(n - i)
        elif (ordem == 'cresc'):
            v.append(i)

    posMax, qnt_cmpout, posMin = minMaxVetor.min_maxVet(v)
    imprimeVetor(v, posMax, posMin)    
    
    posMax, qnt_cmpout, posMin = minMaxVetorII.min_maxVet2(v)
    imprimeVetor(v, posMax, posMin)

    posMax, qnt_cmpout, posMin = minMaxVetorIII.maxMinVetSuperOtim(v)
    imprimeVetor(v, posMax, posMin)


